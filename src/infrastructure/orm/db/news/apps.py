# coding: utf-8

from django.apps import AppConfig


class NewsConfig(AppConfig):
    label = "news"
    name = "src.infrastructure.orm.db.news"
    verbose_name = "News"

    def ready(self):
        from src.infrastructure.orm.db.news.model import News as _model

        _model.register_file_cleanup("image")
