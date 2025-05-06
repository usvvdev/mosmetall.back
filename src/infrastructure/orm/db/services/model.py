# coding: utf-8

from django.db import models as _m

from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import ServicesEntity as _entity
from src.infrastructure.orm.db.mixins.utils import file_size_validator


class Product(_Model):
    name = _m.CharField(max_length=64, null=False, unique=True)
    image = _m.ImageField(
        upload_to="services/products/",
        blank=False,
        null=False,
        validators=[file_size_validator],
        unique=True,
    )
    size = _m.CharField(max_length=32, null=False)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "products"


class Service(_Model):
    name = _m.CharField(max_length=64, null=False, unique=True)
    image = _m.ImageField(
        upload_to="services/",
        blank=False,
        null=False,
        validators=[file_size_validator],
        unique=True,
    )
    subtitle = _m.CharField(max_length=128, null=False)
    description = _m.TextField(null=False)
    quote = _m.CharField(max_length=256, null=False)
    type = _m.CharField(max_length=10, null=False)
    size = _m.CharField(max_length=32, null=False)
    products = _m.ManyToManyField(Product, related_name="services")

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        db_table = "services"

    def __str__(self) -> str:
        return _entity.to_string(self)
