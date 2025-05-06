# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.reviews.factory import (
    ReviewViewSetFactory as _factory,
)
from src.interface.routes.reviews.route import review_router


class ReviewRouter(SimpleRouter):
    routes = [
        Route(
            url=review_router.get_url("review_list"),
            mapping=review_router.map("review_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        )
    ]
