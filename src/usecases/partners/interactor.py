# coding: utf-8

import typing as _t

from src.domain.entities.repositories import PartnerEntity as _entity


class PartnerInteractor:
    def __init__(self, repository: object):
        self.repository = repository

    def get_availables(self) -> _t.List[_entity]:
        return self.repository.get_availables()
