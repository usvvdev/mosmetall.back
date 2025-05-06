# coding: utf-8

from django.apps import AppConfig


class ReviewConfig(AppConfig):
    label = "reviews"
    name = "src.infrastructure.orm.db.reviews"
    verbose_name = "Reviews"

    def ready(self):
        from src.infrastructure.orm.db.reviews.model import Review as _model

        _model.register_file_cleanup("image")
