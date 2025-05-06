# coding: utf-8

import typing as _t

from src.domain.entities.repositories import (
    ServiceEntity as _entity,
    ServicesEntity as _list_entity,
)


class ServiceInteractor:
    def __init__(self, repository: object):
        self.repository = repository

    def get_service(self, service_id: int) -> _entity:
        return self.repository.get_service(service_id)

    def get_availables(self) -> _t.List[_list_entity]:
        return self.repository.get_availables()
