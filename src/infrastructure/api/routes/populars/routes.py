# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.populars.factory import (
    PopularViewSetFactory as _factory,
)
from src.interface.routes.populars.route import popular_router


class PopularRouter(SimpleRouter):
    routes = [
        Route(
            url=popular_router.get_url("popular_list"),
            mapping=popular_router.map("popular_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        )
    ]
