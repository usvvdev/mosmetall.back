# coding: utf-8

from django.db import models as _m

from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import PopularEntity as _entity
from src.infrastructure.orm.db.mixins.utils import file_size_validator


class Popular(_Model):
    name = _m.CharField(null=False, max_length=64, unique=True)
    image = _m.ImageField(
        upload_to="populars/",
        blank=False,
        null=False,
        validators=[file_size_validator],
        unique=True,
    )

    class Meta:
        verbose_name = "popular"
        verbose_name_plural = "populars"
        db_table = "populars"

    def __str__(self) -> str:
        return _entity.to_string(self)
