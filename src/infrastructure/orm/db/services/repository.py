# coding: utf-8

import typing as _t

from src.domain.entities.repositories import (
    ServiceEntity as _service,
    ServicesEntity as _services,
    ProductEntity as _product,
)
from src.interface.repositories.exceptions import EntityDoesNotExist as _exception
from src.infrastructure.orm.db.services.model import Service as _model


class ServiceRepository:
    def __service(self, service: _t.Dict) -> _service:
        return _service(
            **service.__dict__,
            products=(
                _product(**product.__dict__) for product in service.products.all()
            ),
        )

    def get_service(self, service_id: int) -> _service:
        service = _model.objects.prefetch_related("products").get(id=service_id)
        if not service:
            raise _exception(f"Service with id: {service_id} doesn't exist.")
        return self.__service(service)

    def get_availables(self) -> _t.List[_services]:
        return list(
            map(lambda services: _services(**services), _model.objects.values())
        )
