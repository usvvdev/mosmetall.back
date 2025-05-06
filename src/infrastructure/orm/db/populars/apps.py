# coding: utf-8

from django.apps import AppConfig


class PopularConfig(AppConfig):
    label = "populars"
    name = "src.infrastructure.orm.db.populars"
    verbose_name = "Populars"

    def ready(self):
        from src.infrastructure.orm.db.populars.model import Popular as _model

        _model.register_file_cleanup("image")
