# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.populars.admin import PopularAdmin as _admin
from src.infrastructure.orm.db.populars.model import Popular as _model

_a.site.register(_model, _admin)
