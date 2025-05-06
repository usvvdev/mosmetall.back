# coding: utf-8

import typing as _t
import logging as _log
from http import HTTPStatus as _status

from src.usecases.services.interactor import ServiceInteractor as _interactor
from src.interface.serializers.services.serializer import (
    ServiceListSerializer as _list_serializer,
    ServiceSerializer as _serializer,
)
from src.interface.repositories.exceptions import EntityDoesNotExist as _exception

_logger = _log.getLogger(__name__)


class ServiceController:
    def __init__(self, interactor: _interactor):
        self.interactor = interactor

    def get_service(self, service_id: int) -> _t.Tuple[_t.List[str], str]:
        try:
            service = self.interactor.get_service(service_id)
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        return (_serializer.model_dump(service), _status.OK.value)

    def list(self) -> _t.Tuple[_t.List[str], str]:
        try:
            services = self.interactor.get_availables()
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        serialized_data = tuple(
            _list_serializer.model_dump(service) for service in services
        )
        return (serialized_data, _status.OK.value)
