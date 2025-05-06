# coding: utf-8

from src.usecases.catalogs.interactor import CatalogInteractor as _interactor
from src.infrastructure.orm.db.catalogs.repository import (
    CatalogRepository as _repository,
)
from src.interface.controllers.catalogs.controller import (
    CatalogController as _controller,
)


class CatalogRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class CatalogInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = CatalogRepositoryFactory.get()
        return _interactor(repository)


class CatalogViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = CatalogInteractorFactory.get()
        return _controller(interactor)
