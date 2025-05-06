# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.services.routes import ServiceRouter as _router
from src.infrastructure.api.views.services.view import ServiceViewSet as _viewset


service_router = _router()
service_router.register("", viewset=_viewset, basename="services")

urlpatterns = [
    path("", include(service_router.urls)),
]
