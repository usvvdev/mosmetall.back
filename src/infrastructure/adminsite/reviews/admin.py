# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.reviews.model import Review as _model


class ReviewAdmin(_a.ModelAdmin):
    model = _model
    list_display = ("id", "image", "author", "post", "description")
    ordering = ("-id",)
