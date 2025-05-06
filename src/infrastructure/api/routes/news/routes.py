# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.news.factory import (
    NewsViewSetFactory as _factory,
)
from src.interface.routes.news.route import news_router


class NewsRouter(SimpleRouter):
    routes = [
        Route(
            url=news_router.get_url("news_list"),
            mapping=news_router.map("news_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        )
    ]
