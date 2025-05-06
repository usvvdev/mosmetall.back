# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.catalogs.routes import CatalogRouter as _router
from src.infrastructure.api.views.catalogs.view import CatalogViewSet as _viewset


catalog_router = _router()
catalog_router.register("", viewset=_viewset, basename="catalogs")

urlpatterns = [
    path("", include(catalog_router.urls)),
]
