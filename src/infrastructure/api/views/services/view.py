# coding: utf-8

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.interface.controllers.services.controller import (
    ServiceController as _controller,
)


class ServiceViewSet(ViewSet):
    viewset_factory = None

    @property
    def controller(self) -> _controller:
        return self.viewset_factory.create()

    def get_service(
        self, request: Request, service_id: int, *args, **kwargs
    ) -> Response:
        payload, status = self.controller.get_service(service_id)
        return Response(data=payload, status=status)

    def list(self, request: Request, *args, **kwargs) -> Response:
        payload, status = self.controller.list()
        return Response(data=payload, status=status)
