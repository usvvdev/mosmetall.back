# coding: utf-8

import typing as _t

from src.domain.entities.repositories import (
    CatalogEntity as _catalog,
    CategoriesEntity as _categories,
    SectionsEntity as _sections,
    CategoryEntity as _category,
    SectionEntity as _section,
    ItemEntity as _item,
    SearchEntity as _search,
)
from src.interface.repositories.exceptions import EntityDoesNotExist as _exception
from src.infrastructure.orm.db.catalogs.model import (
    Catalog as _catalog_m,
    Category as _category_m,
    Section as _section_m,
    Item as _item_m,
)
from src.domain.core.constants import FILTER_PARAMS


class CatalogRepository:
    def __category(self, category_id: int) -> _category_m:
        category = _category_m.objects.prefetch_related("sections").get(id=category_id)
        if not category:
            raise _exception(f"Category with id: {category_id} doesn't exist.")
        return category

    def __section(self, category_id: int, section_id: int) -> _section_m:
        section = self.__category(category_id).sections.filter(id=section_id).first()
        if not section:
            raise _exception(
                f"Section '{section_id}' doesn't exist in category with id: {category_id}."
            )
        return section

    def __categories(self, category: _t.Dict) -> _categories:
        return _categories(
            **category.__dict__,
            sections=[
                _sections(**section.__dict__) for section in category.sections.all()
            ],
        )

    def __catalog(self, catalog: _t.Dict) -> _catalog:
        return _catalog(
            **catalog.__dict__,
            categories=[
                self.__categories(category) for category in catalog.categories.all()
            ],
        )

    def get_category(self, category_id: int) -> _category:
        category = self.__category(category_id)
        return _category(
            **category.__dict__,
            sections=(
                _sections(**section.__dict__) for section in category.sections.all()
            ),
        )

    def get_section(
        self, category_id: int, section_id: int, filters: _t.Dict
    ) -> _section:
        section = self.__section(category_id, section_id)
        if not section:
            raise _exception(f"Section with name: {section_id} doesn't exist.")
        filter_args = {
            f"{key}__in": filters[key] for key in FILTER_PARAMS if filters[key]
        }
        items = section.items.all().filter(**filter_args)
        filtered_section = _section(
            **section.__dict__,
            items=[_item(**item.__dict__) for item in items],
        )
        filtered_section.set_filters()
        return filtered_section

    def get_availables(self) -> _t.List[_catalog]:
        return list(
            map(
                lambda catalog: self.__catalog(catalog),
                _catalog_m.objects.prefetch_related("categories__sections"),
            )
        )

    def search_by_name(self, item_name: str, filters: _t.Dict) -> _t.List[_search]:
        items = _item_m.objects.filter(name__iregex=item_name)
        if not items:
            raise _exception(f"Items with name: {item_name} doesn't exist.")
        filter_args = {f"{key}__in": filters[key] for key in filters if filters[key]}
        filtred_search = _search(
            items=[_item(**item.__dict__) for item in items.filter(**filter_args)]
        )
        filtred_search.set_filters()
        return filtred_search
