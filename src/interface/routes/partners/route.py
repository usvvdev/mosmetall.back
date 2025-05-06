# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import PARTNER_PREFIX
from src.interface.controllers.partners.controller import (
    PartnerController as _controller,
)


partner_router = Router()
partner_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{PARTNER_PREFIX}",
            controller=_controller,
            method="list",
            name="partner_list",
        ),
    ]
)
