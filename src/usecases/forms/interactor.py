# coding: utf-8

from src.domain.entities.repositories import FormEntity as _entity
from src.interface.controllers.forms.utils import FormUtils as _utils


class FormInteractor:
    def send_email(self, data: dict) -> _entity:
        return _utils.send_email(data)
