# coding: utf-8

import logging as _log
import typing as _t
from http import HTTPStatus as _status

from src.usecases.catalogs.interactor import CatalogInteractor as _interactor
from src.interface.serializers.catalogs.serializer import (
    CatalogSerializer as _catalog,
    SectionSerializer as _section,
    SearchSerilzer as _search,
)
from src.interface.controllers.catalogs.utils import SectionUtils as _utils
from src.interface.repositories.exceptions import EntityDoesNotExist as _exception


_logger = _log.getLogger(__name__)


class CatalogController:
    def __init__(self, interactor: _interactor):
        self.interactor = interactor

    def get_category(self, category_id: int) -> _t.Tuple[_t.List[str], str]:
        try:
            category = self.interactor.get_category(category_id)
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        return (_catalog.model_dump(category), _status.OK.value)

    def get_section(
        self, page: int, category_id: int, section_id: int, filters: _t.Dict
    ) -> _t.Tuple[_t.List[str], str]:
        try:
            section = self.interactor.get_section(category_id, section_id, filters)
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        _utils.paginated_section(section, page)
        return (_section.model_dump(section), _status.OK.value)

    def list(self) -> _t.Tuple[_t.List[str], str]:
        try:
            catalogs = self.interactor.get_availables()
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        serialized_data = tuple(_catalog.model_dump(catalog) for catalog in catalogs)
        return (serialized_data, _status.OK.value)

    def search_items(
        self, page: int, item_name: str, filters: _t.Dict
    ) -> _t.Tuple[_t.List[str], str]:
        try:
            items = self.interactor.search_items(item_name, filters)
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
            return ([], _status.OK.value)
        _utils.paginated_search(items, page)
        return (_search.model_dump(items), _status.OK.value)
