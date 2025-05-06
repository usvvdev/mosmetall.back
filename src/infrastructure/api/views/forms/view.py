# coding: utf-8

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.interface.controllers.forms.controller import (
    FormController as _controller,
)


class FormViewSet(ViewSet):
    viewset_factory = None

    @property
    def controller(self) -> _controller:
        return self.viewset_factory.create()

    def send_email(self, request: Request, *args, **kwargs) -> Response:
        data = dict(request.data)
        data["files"] = request.FILES.getlist("files", [])
        payload, status = self.controller.send_email(data)
        return Response(data=payload, status=status)
