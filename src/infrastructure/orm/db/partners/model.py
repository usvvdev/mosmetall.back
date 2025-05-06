# coding: utf-8

from django.db import models as _m

from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import PartnerEntity as _entity
from src.infrastructure.orm.db.mixins.utils import file_size_validator


class Partner(_Model):
    image = _m.ImageField(
        upload_to="partners/",
        blank=False,
        null=False,
        validators=[file_size_validator],
        unique=True,
    )
    name = _m.CharField(max_length=64, null=False, unique=True)

    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"
        db_table = "partners"

    def __str__(self) -> str:
        return _entity.to_string(self)
