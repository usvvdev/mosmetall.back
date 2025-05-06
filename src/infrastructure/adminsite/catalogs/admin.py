# coding: utf-8
from django.contrib import admin as _a

from src.infrastructure.orm.db.catalogs.model import (
    Catalog as _catalog,
    Category as _category,
    Section as _section,
    Item as _item,
)


class CatalogAdmin(_a.ModelAdmin):
    model = _catalog
    list_display = ("id", "categories_name")
    ordering = ("-id",)

    def categories_name(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])


class CategoryAdmin(_a.ModelAdmin):
    model = _category
    list_display = ("id", "name", "sections_count")
    ordering = ("-id",)

    def sections_count(self, obj):
        return obj.sections.count()


class SectionAdmin(_a.ModelAdmin):
    model = _section
    list_display = ("id", "name", "items_count")
    ordering = ("-id",)

    def items_count(self, obj):
        return obj.items.count()


class ItemAdmin(_a.ModelAdmin):
    model = _item
    list_display = (
        "id",
        "name",
        "type",
        "stamp",
        "gost",
        "size",
        "diameter",
        "length",
        "width",
        "thickness",
        "side",
        "nominal_diameter",
        "nominal_pressure",
        "material",
    )
    ordering = ("-id",)
