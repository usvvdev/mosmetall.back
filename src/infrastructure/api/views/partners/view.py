# coding: utf-8

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.interface.controllers.partners.controller import (
    PartnerController as _controller,
)


class PartnerViewSet(ViewSet):
    viewset_factory = None

    @property
    def controller(self) -> _controller:
        return self.viewset_factory.create()

    def list(self, request: Request, *args, **kwargs) -> Response:
        payload, status = self.controller.list()
        return Response(data=payload, status=status)
