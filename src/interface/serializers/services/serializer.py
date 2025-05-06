# coding: utf-8

from src.domain.entities.repositories import (
    ServiceEntity as _entity,
    ServicesEntity as _list_entity,
)


class ServiceListSerializer(_list_entity):
    pass


class ServiceSerializer(_entity):
    pass
