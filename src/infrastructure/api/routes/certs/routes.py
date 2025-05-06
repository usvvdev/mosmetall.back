# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.certs.factory import (
    CertViewSetFactory as _factory,
)
from src.interface.routes.certs.route import cert_router


class CertRouter(SimpleRouter):
    routes = [
        Route(
            url=cert_router.get_url("cert_list"),
            mapping=cert_router.map("cert_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        )
    ]
