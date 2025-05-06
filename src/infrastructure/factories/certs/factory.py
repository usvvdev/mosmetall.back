# coding: utf-8

from src.usecases.certs.interactor import CertInteractor as _interactor
from src.infrastructure.orm.db.certs.repository import (
    CertRepository as _repository,
)
from src.interface.controllers.certs.controller import (
    CertController as _controller,
)


class CertRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class CertInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = CertRepositoryFactory.get()
        return _interactor(repository)


class CertViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = CertInteractorFactory.get()
        return _controller(interactor)
