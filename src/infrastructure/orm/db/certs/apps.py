# coding: utf-8

from django.apps import AppConfig


class CertConfig(AppConfig):
    label = "certs"
    name = "src.infrastructure.orm.db.certs"
    verbose_name = "Certificates"

    def ready(self):
        from src.infrastructure.orm.db.certs.model import Cert as _model

        _model.register_file_cleanup("file")
