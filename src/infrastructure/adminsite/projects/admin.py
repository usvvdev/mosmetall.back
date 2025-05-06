# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.projects.model import Project as _model


class ProjectAdmin(_a.ModelAdmin):
    model = _model
    list_display = ("id", "image", "title", "location")
    ordering = ("-id",)
