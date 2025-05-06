# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import CERT_PREFIX
from src.interface.controllers.certs.controller import (
    CertController as _controller,
)


cert_router = Router()
cert_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{CERT_PREFIX}",
            controller=_controller,
            method="list",
            name="cert_list",
        )
    ]
)
