# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import REVIEW_PREFIX
from src.interface.controllers.reviews.controller import (
    ReviewController as _controller,
)


review_router = Router()
review_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{REVIEW_PREFIX}",
            controller=_controller,
            method="list",
            name="review_list",
        ),
    ]
)
