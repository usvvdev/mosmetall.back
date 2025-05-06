# coding: utf-8

from django.apps import AppConfig


class ProjectConfig(AppConfig):
    label = "projects"
    name = "src.infrastructure.orm.db.projects"
    verbose_name = "Projects"

    def ready(self):
        from src.infrastructure.orm.db.projects.model import Project as _model

        _model.register_file_cleanup("image")
