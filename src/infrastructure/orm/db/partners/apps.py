# coding: utf-8

from django.apps import AppConfig


class PartnerConfig(AppConfig):
    label = "partners"
    name = "src.infrastructure.orm.db.partners"
    verbose_name = "Partners"

    def ready(self):
        from src.infrastructure.orm.db.partners.model import Partner as _model

        _model.register_file_cleanup("image")
