# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.news.routes import NewsRouter as _router
from src.infrastructure.api.views.news.view import NewsViewSet as _viewset


news_router = _router()
news_router.register("", viewset=_viewset, basename="news")

urlpatterns = [
    path("", include(news_router.urls)),
]
