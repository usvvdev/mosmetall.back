# coding: utf-8

from django.db import models as _m

from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import NewsEntity as _entity
from src.infrastructure.orm.db.mixins.utils import file_size_validator


class News(_Model):
    image = _m.ImageField(
        upload_to="news/",
        null=False,
        validators=[file_size_validator],
        unique=True,
    )
    title = _m.CharField(max_length=64, null=False, unique=True)
    description = _m.CharField(max_length=128, null=False)
    type = _m.CharField(max_length=32, null=True)
    link = _m.CharField(max_length=256, null=False, blank=True, unique=True)
    date = _m.DateField(null=False)

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"
        db_table = "news"

    def __str__(self) -> str:
        return _entity.to_string(self)
