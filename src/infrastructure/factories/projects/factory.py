# coding: utf-8

from src.usecases.projects.interactor import ProjectInteractor as _interactor
from src.infrastructure.orm.db.projects.repository import (
    ProjectsRepository as _repository,
)
from src.interface.controllers.projects.controller import (
    ProjectController as _controller,
)


class ProjectRepositoryFactory:
    @staticmethod
    def get() -> _repository:
        return _repository()


class ProjectInteractorFactory:
    @staticmethod
    def get() -> _interactor:
        repository = ProjectRepositoryFactory.get()
        return _interactor(repository)


class ProjectViewSetFactory:
    @staticmethod
    def create() -> _controller:
        interactor = ProjectInteractorFactory.get()
        return _controller(interactor)
