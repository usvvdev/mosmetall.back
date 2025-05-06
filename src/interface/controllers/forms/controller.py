# coding: utf-8

import typing as _t
import logging as _log
from http import HTTPStatus as _status

from src.usecases.forms.interactor import FormInteractor as _interactor
from src.interface.repositories.exceptions import EntityDoesNotExist as _exception

_logger = _log.getLogger(__name__)


class FormController:
    def __init__(self, interactor: _interactor):
        self.interactor = interactor

    def send_email(self, data: dict) -> _t.Tuple[_t.List[str], str]:
        try:
            self.interactor.send_email(data)
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        return (
            "Message was send succsesful.",
            _status.OK.value,
        )
