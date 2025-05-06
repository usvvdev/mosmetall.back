# coding: utf-8

import typing as _t

from src.domain.entities.repositories import NewsEntity as _entity


class NewsInteractor:
    def __init__(self, repository: object):
        self.repository = repository

    def get_availables(self) -> _t.List[_entity]:
        return self.repository.get_availables()
