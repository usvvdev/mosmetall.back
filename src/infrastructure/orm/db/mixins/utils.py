# coding: utf-8

from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError as _exception


def file_size_validator(file: UploadedFile):
    limit_kb = 100
    if file.size > limit_kb * 1024 * 1024:
        raise _exception(f"File size should not exceed {limit_kb}MB.")
