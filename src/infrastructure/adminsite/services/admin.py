# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.services.model import (
    Product as _product,
    Service as _service,
)


class ProductAdmin(_a.ModelAdmin):
    model = _product
    list_display = ("id", "name", "image", "size")
    ordering = ("-id",)


class ServiceAdmin(_a.ModelAdmin):
    model = _service
    list_display = ("id", "name", "image", "type", "size", "products_name")
    ordering = ("-id",)

    def products_name(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
