# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.partners.factory import (
    PartnerViewSetFactory as _factory,
)
from src.interface.routes.partners.route import partner_router


class PartnerRouter(SimpleRouter):
    routes = [
        Route(
            url=partner_router.get_url("partner_list"),
            mapping=partner_router.map("partner_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        )
    ]
