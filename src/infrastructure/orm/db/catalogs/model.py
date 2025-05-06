# coding: utf-8

from django.db import models as _m

from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import (
    CatalogEntity as _catalog,
    CategoriesEntity as _categories,
    SectionEntity as _section,
)


class Item(_Model):
    name = _m.CharField(max_length=64, null=False)
    type = _m.CharField(max_length=32, null=True, blank=True)
    stamp = _m.CharField(max_length=64, null=True, blank=True)
    gost = _m.CharField(max_length=32, null=True, blank=True)
    size = _m.CharField(max_length=16, null=True, blank=True)
    diameter = _m.CharField(max_length=16, null=True, blank=True)
    length = _m.CharField(max_length=16, null=True, blank=True)
    width = _m.CharField(max_length=16, null=True, blank=True)
    thickness = _m.CharField(max_length=16, null=True, blank=True)
    side = _m.CharField(max_length=16, null=True, blank=True)
    nominal_diameter = _m.CharField(max_length=16, null=True, blank=True)
    nominal_pressure = _m.CharField(max_length=16, null=True, blank=True)
    material = _m.CharField(max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        db_table = "items"

    def __str__(self):
        return self.name


class Section(_Model):
    name = _m.CharField(max_length=64, null=False, unique=True)
    items = _m.ManyToManyField(Item, related_name="items")

    class Meta:
        verbose_name = "section"
        verbose_name_plural = "sections"
        db_table = "sections"

    def __str__(self):
        return _section.to_string(self)


class Category(_Model):
    name = _m.CharField(max_length=64, null=False, unique=True)
    sections = _m.ManyToManyField(Section, related_name="sections")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        db_table = "categories"

    def __str__(self):
        return _categories.to_string(self)


class Catalog(_Model):
    categories = _m.ManyToManyField(Category, related_name="categories")

    class Meta:
        verbose_name = "catalog"
        verbose_name_plural = "catalogs"
        db_table = "catalogs"

    def __str__(self) -> str:
        return _catalog.to_string(self)
