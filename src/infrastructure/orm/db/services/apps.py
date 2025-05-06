# coding: utf-8

from django.apps import AppConfig


class ServiceConfig(AppConfig):
    label = "services"
    name = "src.infrastructure.orm.db.services"
    verbose_name = "Services"

    def ready(self):
        from src.infrastructure.orm.db.services.model import (
            Service as _service,
            Product as _product,
        )

        [_model.register_file_cleanup("image") for _model in (_service, _product)]
