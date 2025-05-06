# coding: utf-8

from src.usecases.reviews.interactor import ReviewInteractor as _interactor
from src.infrastructure.orm.db.reviews.repository import (
    ReviewRepository as _repository,
)
from src.interface.controllers.reviews.controller import (
    ReviewController as _controller,
)


class ReviewRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class ReviewInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = ReviewRepositoryFactory.get()
        return _interactor(repository)


class ReviewViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = ReviewInteractorFactory.get()
        return _controller(interactor)
