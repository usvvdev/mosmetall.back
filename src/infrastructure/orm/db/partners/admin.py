# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.partners.admin import PartnerAdmin as _admin
from src.infrastructure.orm.db.partners.model import Partner as _model

_a.site.register(_model, _admin)
