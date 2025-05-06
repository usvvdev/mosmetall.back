# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.forms.routes import FormRouter as _router
from src.infrastructure.api.views.forms.view import FormViewSet as _viewset


form_router = _router()
form_router.register("", viewset=_viewset, basename="forms")

urlpatterns = [
    path("", include(form_router.urls)),
]
