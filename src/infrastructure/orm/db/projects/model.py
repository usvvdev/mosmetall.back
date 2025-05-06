# coding: utf-8

from django.db import models as _m

from src.infrastructure.orm.db.mixins.model import MixinModel as _Model
from src.domain.entities.repositories import ProjectEntity as _entity
from src.infrastructure.orm.db.mixins.utils import file_size_validator


class Project(_Model):
    image = _m.ImageField(
        upload_to="projects/",
        blank=False,
        null=False,
        validators=[file_size_validator],
        unique=True,
    )
    title = _m.CharField(max_length=128, null=False, unique=True)
    location = _m.CharField(max_length=64, null=False)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        db_table = "projects"

    def __str__(self) -> str:
        return _entity.to_string(self)
