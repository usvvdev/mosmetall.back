# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.reviews.admin import ReviewAdmin as _admin
from src.infrastructure.orm.db.reviews.model import Review as _model

_a.site.register(_model, _admin)
