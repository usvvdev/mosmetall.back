# coding: utf-8

from src.domain.core.constants import HTTP_VERB_POST
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import EMAIL_PREFIX
from src.interface.controllers.forms.controller import (
    FormController as _controller,
)


form_router = Router()
form_router.register(
    [
        Route(
            http_verb=HTTP_VERB_POST,
            path=rf"^{EMAIL_PREFIX}",
            controller=_controller,
            method="send_email",
            name="form_send_email",
        )
    ]
)
