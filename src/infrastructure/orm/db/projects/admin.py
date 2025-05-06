# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.projects.admin import ProjectAdmin as _admin
from src.infrastructure.orm.db.projects.model import Project as _model

_a.site.register(_model, _admin)
