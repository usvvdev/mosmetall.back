# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.partners.model import Partner as _model


class PartnerAdmin(_a.ModelAdmin):
    model = _model
    list_display = ("id", "image", "name")
    ordering = ("-id",)
