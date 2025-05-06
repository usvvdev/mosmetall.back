# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.services.factory import (
    ServiceViewSetFactory as _factory,
)
from src.interface.routes.services.route import service_router


class ServiceRouter(SimpleRouter):
    routes = [
        Route(
            url=service_router.get_url("service_get"),
            mapping=service_router.map("service_get"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-get",
            detail=False,
        ),
        Route(
            url=service_router.get_url("service_list"),
            mapping=service_router.map("service_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        ),
    ]
