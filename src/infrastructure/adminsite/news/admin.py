# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.news.model import News as _model


class NewsAdmin(_a.ModelAdmin):
    model = _model
    list_display = ("id", "image", "title", "description", "type", "link", "date")
    ordering = ("-date",)
