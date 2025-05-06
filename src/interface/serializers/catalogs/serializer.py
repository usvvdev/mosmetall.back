# coding: utf-8

from src.domain.entities.repositories import (
    CatalogEntity as _catalog,
    CategoryEntity as _category,
    SectionEntity as _section,
    ItemEntity as _item,
    SearchEntity as _search,
)


class CatalogSerializer(_catalog):
    pass


class CategorySerializer(_category):
    pass


class SectionSerializer(_section):
    pass


class ItemSerializer(_item):
    pass


class SearchSerilzer(_search):
    pass
