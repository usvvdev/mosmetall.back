# coding: utf-8

from django.conf import settings
from django.conf.urls import include
from django.urls import path

from src.domain.core.constants import PROJECT_APPS

urlpatterns = list(
    map(
        lambda app: path("", include(f"{settings.API_ROUTES}.{app}.urls")),
        PROJECT_APPS,
    )
)
