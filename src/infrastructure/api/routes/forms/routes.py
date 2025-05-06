# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.forms.factory import (
    FormViewSetFactory as _factory,
)
from src.interface.routes.forms.route import form_router


class FormRouter(SimpleRouter):
    routes = [
        Route(
            url=form_router.get_url("form_send_email"),
            mapping=form_router.map("form_send_email"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        )
    ]
