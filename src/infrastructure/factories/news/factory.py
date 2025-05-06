# coding: utf-8

from src.usecases.news.interactor import NewsInteractor as _interactor
from src.infrastructure.orm.db.news.repository import (
    NewsRepository as _repository,
)
from src.interface.controllers.news.controller import (
    NewsController as _controller,
)


class NewsRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class NewsInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = NewsRepositoryFactory.get()
        return _interactor(repository)


class NewsViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = NewsInteractorFactory.get()
        return _controller(interactor)
