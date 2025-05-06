# coding: utf-8

from django.db import models as _m

from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import ReviewEntity as _entity
from src.infrastructure.orm.db.mixins.utils import file_size_validator


class Review(_Model):
    image = _m.ImageField(
        upload_to="reviews/",
        blank=False,
        null=False,
        validators=[file_size_validator],
        unique=True,
    )
    author = _m.CharField(max_length=32, null=False, unique=True)
    post = _m.TextField(null=False, unique=True)
    description = _m.CharField(max_length=128, null=False)

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        db_table = "reviews"

    def __str__(self) -> str:
        return _entity.to_string(self)
