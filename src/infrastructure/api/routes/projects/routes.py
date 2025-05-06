# coding: utf-8

from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.projects.factory import (
    ProjectViewSetFactory as _factory,
)
from src.interface.routes.projects.route import project_router


class ProjectRouter(SimpleRouter):
    routes = [
        Route(
            url=project_router.get_url("project_list"),
            mapping=project_router.map("project_list"),
            initkwargs={"viewset_factory": _factory},
            name="{basename}-list",
            detail=False,
        )
    ]
