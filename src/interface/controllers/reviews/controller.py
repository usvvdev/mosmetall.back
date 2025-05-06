# coding: utf-8

import typing as _t
import logging as _log
from http import HTTPStatus as _status

from src.usecases.reviews.interactor import ReviewInteractor as _interactor
from src.interface.serializers.reviews.serializer import (
    ReviewSerializer as _serializer,
)
from src.interface.repositories.exceptions import EntityDoesNotExist as _exception

_logger = _log.getLogger(__name__)


class ReviewController:
    def __init__(self, interactor: _interactor):
        self.interactor = interactor

    def list(self) -> _t.Tuple[_t.List[str], str]:
        try:
            reviews = self.interactor.get_availables()
        except _exception as err:
            _logger.error({__class__.__name__: "{e}".format(e=err)})
        serialized_data = tuple(_serializer.model_dump(review) for review in reviews)
        return (serialized_data, _status.OK.value)
