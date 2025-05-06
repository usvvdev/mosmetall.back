# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.catalogs.factory import (
    CatalogViewSetFactory as _factory,
)
from src.interface.routes.catalogs.route import catalog_router


class CatalogRouter(SimpleRouter):
    routes = [
        Route(
            url=catalog_router.get_url("section_get"),
            mapping=catalog_router.map("section_get"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-get",
            detail=False,
        ),
        Route(
            url=catalog_router.get_url("category_get"),
            mapping=catalog_router.map("category_get"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-get",
            detail=False,
        ),
        Route(
            url=catalog_router.get_url("catalog_list"),
            mapping=catalog_router.map("catalog_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        ),
        Route(
            url=catalog_router.get_url("search_item"),
            mapping=catalog_router.map("search_item"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-search",
            detail=False,
        ),
    ]
