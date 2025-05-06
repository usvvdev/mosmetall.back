# coding: utf-8

from django.db import models as _m
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage


class MixinModel(_m.Model):
    id = _m.AutoField(primary_key=True)
    file_field_name = None

    class Meta:
        abstract = True

    @classmethod
    def register_file_cleanup(cls, file_field_name: str):
        cls.file_field_name = file_field_name

        @receiver(post_delete, sender=cls)
        def delete_file(sender, instance, **kwargs):
            file_field = getattr(instance, cls.file_field_name)
            if file_field:
                if default_storage.exists(file_field.name):
                    default_storage.delete(file_field.name)
