# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import NEWS_PREFIX
from src.interface.controllers.news.controller import (
    NewsController as _controller,
)


news_router = Router()
news_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{NEWS_PREFIX}",
            controller=_controller,
            method="list",
            name="news_list",
        ),
    ]
)
