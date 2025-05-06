# coding: utf-8

from django.core.paginator import Paginator as _paginator
from src.interface.serializers.catalogs.serializer import (
    SectionSerializer as _section,
    SearchSerilzer as _search,
)


class SectionUtils:
    showed_items = 10

    @classmethod
    def paginated_section(cls, section: _section, page: int):
        paginator = _paginator(section.items, cls.showed_items)
        section.items, section.current_page, section.total_items = (
            paginator.get_page(page).object_list,
            page,
            paginator.count,
        )

    @classmethod
    def paginated_search(cls, search: _search, page: int):
        paginator = _paginator(search.items, cls.showed_items)
        search.items, search.current_page, search.total_items = (
            paginator.get_page(page).object_list,
            page,
            paginator.count,
        )
