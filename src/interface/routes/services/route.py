# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import SERVICE_PREFIX
from src.interface.controllers.services.controller import (
    ServiceController as _controller,
)


service_router = Router()
service_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{SERVICE_PREFIX}",
            controller=_controller,
            method="list",
            name="service_list",
        ),
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{SERVICE_PREFIX}/(?P<service_id>[a-zA-Z0-9_]+)",
            controller=_controller,
            method="get_service",
            name="service_get",
        ),
    ]
)
