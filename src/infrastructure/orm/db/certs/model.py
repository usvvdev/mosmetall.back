# coding: utf-8

from django.db import models as _m
from django.core.validators import FileExtensionValidator as _validator

from src.domain.core.constants import FILE_TYPE, EXTENSION_FILE_TYPES
from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import CertEntity as _entity
from src.infrastructure.orm.db.mixins.utils import file_size_validator


class Cert(_Model):
    file = _m.FileField(
        upload_to="certs/",
        null=False,
        validators=[_validator(allowed_extensions=FILE_TYPE), file_size_validator],
        unique=True,
    )
    title = _m.CharField(max_length=64, null=False, unique=True)
    type = _m.CharField(max_length=10, null=False)

    class Meta:
        verbose_name = "certificate"
        verbose_name_plural = "certificates"
        db_table = "certs"

    def save(self, *args, **kwargs):
        self.type = EXTENSION_FILE_TYPES.get(
            self.file.name.split(".")[-1].lower(), None
        )
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return _entity.to_string(self)
