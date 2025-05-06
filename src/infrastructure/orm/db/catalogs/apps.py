# coding: utf-8

from django.apps import AppConfig


class CatalogConfig(AppConfig):
    label = "catalogs"
    name = "src.infrastructure.orm.db.catalogs"
    verbose_name = "Catalogs"
