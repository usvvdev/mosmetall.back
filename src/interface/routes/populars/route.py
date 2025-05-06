# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import POPULAR_PREFIX
from src.interface.controllers.populars.controller import (
    PopularController as _controller,
)


popular_router = Router()
popular_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{POPULAR_PREFIX}",
            controller=_controller,
            method="list",
            name="popular_list",
        ),
    ]
)
