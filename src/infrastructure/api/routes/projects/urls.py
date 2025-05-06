# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.projects.routes import ProjectRouter as _router
from src.infrastructure.api.views.projects.view import ProjectViewSet as _viewset


project_router = _router()
project_router.register("", viewset=_viewset, basename="projects")

urlpatterns = [
    path("", include(project_router.urls)),
]
