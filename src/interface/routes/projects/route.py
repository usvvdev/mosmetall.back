# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import PROJECT_PREFIX
from src.interface.controllers.projects.controller import (
    ProjectController as _controller,
)


project_router = Router()
project_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{PROJECT_PREFIX}",
            controller=_controller,
            method="list",
            name="project_list",
        ),
    ]
)
