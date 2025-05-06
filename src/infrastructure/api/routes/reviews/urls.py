# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.reviews.routes import ReviewRouter as _router
from src.infrastructure.api.views.reviews.view import ReviewViewSet as _viewset


review_router = _router()
review_router.register("", viewset=_viewset, basename="reviews")

urlpatterns = [
    path("", include(review_router.urls)),
]
