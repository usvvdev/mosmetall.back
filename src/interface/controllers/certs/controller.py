# coding: utf-8

import logging as _log
import typing as _t
from http import HTTPStatus as _status

from src.usecases.certs.interactor import CertInteractor as _interactor
from src.interface.serializers.certs.serializer import (
    CertSerializer as _serializer,
)
from src.interface.repositories.exceptions import EntityDoesNotExist as _exception

_logger = _log.getLogger(__name__)


class CertController:
    def __init__(self, interactor: _interactor):
        self.interactor = interactor

    def list(self) -> _t.Tuple[_t.List[str], str]:
        try:
            certs = self.interactor.get_availables()
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        serialized_data = tuple(_serializer.model_dump(cert) for cert in certs)
        return (serialized_data, _status.OK.value)
