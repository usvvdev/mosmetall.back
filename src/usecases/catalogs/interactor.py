# coding: utf-8

import typing as _t

from src.domain.entities.repositories import (
    CatalogEntity as _entity,
    SectionEntity as _section,
    SearchEntity as _search,
)


class CatalogInteractor:
    def __init__(self, repository: object):
        self.repository = repository

    def get_category(self, category_id: int) -> _entity:
        return self.repository.get_category(category_id)

    def get_section(
        self, category_id: int, section_id: int, filters: _t.Dict
    ) -> _section:
        return self.repository.get_section(category_id, section_id, filters)

    def get_availables(self) -> _t.List[_entity]:
        return self.repository.get_availables()

    def search_items(self, item_name: str, filters: _t.Dict) -> _t.List[_search]:
        return self.repository.search_by_name(item_name, filters)
