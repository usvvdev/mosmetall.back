# coding: utf-8

from src.usecases.services.interactor import ServiceInteractor as _interactor
from src.infrastructure.orm.db.services.repository import (
    ServiceRepository as _repository,
)
from src.interface.controllers.services.controller import (
    ServiceController as _controller,
)


class ServiceRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class ServiceInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = ServiceRepositoryFactory.get()
        return _interactor(repository)


class ServiceViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = ServiceInteractorFactory.get()
        return _controller(interactor)
