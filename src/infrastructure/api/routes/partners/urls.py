# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.partners.routes import PartnerRouter as _router
from src.infrastructure.api.views.partners.view import PartnerViewSet as _viewset


partner_router = _router()
partner_router.register("", viewset=_viewset, basename="partners")

urlpatterns = [
    path("", include(partner_router.urls)),
]
