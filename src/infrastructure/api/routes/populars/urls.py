# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.populars.routes import PopularRouter as _router
from src.infrastructure.api.views.populars.view import PopularViewSet as _viewset


popular_router = _router()
popular_router.register("", viewset=_viewset, basename="populars")

urlpatterns = [
    path("", include(popular_router.urls)),
]
