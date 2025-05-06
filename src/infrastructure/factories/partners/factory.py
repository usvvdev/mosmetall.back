# coding: utf-8

from src.usecases.partners.interactor import PartnerInteractor as _interactor
from src.infrastructure.orm.db.partners.repository import (
    PartnerRepository as _repository,
)
from src.interface.controllers.partners.controller import (
    PartnerController as _controller,
)


class PartnerRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class PartnerInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = PartnerRepositoryFactory.get()
        return _interactor(repository)


class PartnerViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = PartnerInteractorFactory.get()
        return _controller(interactor)
