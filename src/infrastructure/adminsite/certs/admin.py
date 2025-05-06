# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.certs.model import Cert as _model


class CertAdmin(_a.ModelAdmin):
    model = _model
    list_display = ("id", "file", "title")
    exclude = ("type",)
    ordering = ("-id",)
