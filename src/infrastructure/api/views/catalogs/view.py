# coding: utf-8

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.interface.controllers.catalogs.controller import (
    CatalogController as _controller,
)
from src.domain.core.constants import FILTER_PARAMS


class CatalogViewSet(ViewSet):
    viewset_factory = None
    default_page = 1

    @property
    def controller(self) -> _controller:
        return self.viewset_factory.create()

    def get_category(
        self, request: Request, category_id: int, *args, **kwargs
    ) -> Response:
        payload, status = self.controller.get_category(category_id)
        return Response(data=payload, status=status)

    def get_section(
        self, request: Request, category_id: int, section_id: int, *args, **kwargs
    ) -> Response:
        page = int(request.GET.get("page", self.default_page))
        filters = {key: request.GET.getlist(key) for key in FILTER_PARAMS}
        payload, status = self.controller.get_section(
            page, category_id, section_id, filters
        )
        return Response(data=payload, status=status)

    def list(self, request: Request, *args, **kwargs) -> Response:
        payload, status = self.controller.list()
        return Response(data=payload, status=status)

    def search_items(self, request: Request, *args, **kwargs) -> Response:
        page = int(request.GET.get("page", self.default_page))
        item_name = request.GET.get("q")
        filters = {key: request.GET.getlist(key) for key in FILTER_PARAMS}
        payload, status = self.controller.search_items(
            page, item_name, filters
        )  # ignore
        return Response(data=payload, status=status)
