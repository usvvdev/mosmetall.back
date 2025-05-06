# coding: utf-8

from src.usecases.populars.interactor import PopularInteractor as _interactor
from src.infrastructure.orm.db.populars.repository import (
    PopularRepository as _repository,
)
from src.interface.controllers.populars.controller import (
    PopularController as _controller,
)


class PopularRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class PopularInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = PopularRepositoryFactory.get()
        return _interactor(repository)


class PopularViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = PopularInteractorFactory.get()
        return _controller(interactor)
