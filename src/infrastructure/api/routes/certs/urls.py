# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.certs.routes import CertRouter as _router
from src.infrastructure.api.views.certs.view import CertViewSet as _viewset


cert_router = _router()
cert_router.register("", viewset=_viewset, basename="certs")

urlpatterns = [
    path("", include(cert_router.urls)),
]
