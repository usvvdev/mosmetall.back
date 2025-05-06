# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.news.admin import NewsAdmin as _admin
from src.infrastructure.orm.db.news.model import News as _model

_a.site.register(_model, _admin)
