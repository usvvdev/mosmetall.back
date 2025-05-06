# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.certs.admin import CertAdmin as _admin
from src.infrastructure.orm.db.certs.model import Cert as _model

_a.site.register(_model, _admin)
