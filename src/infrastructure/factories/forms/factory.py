# coding: utf-8

from src.usecases.forms.interactor import FormInteractor as _interactor
from src.interface.controllers.forms.controller import (
    FormController as _controller,
)


class FormInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        return _interactor()


class FormViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = FormInteractorFactory.get()
        return _controller(interactor)
