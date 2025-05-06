# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.populars.model import Popular as _model


class PopularAdmin(_a.ModelAdmin):
    model = _model
    list_display = ("id", "name", "image")
    ordering = ("-id",)
