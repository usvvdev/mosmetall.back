# coding: utf-8

import typing as _t

from src.domain.entities.repositories import NewsEntity as _entity
from src.infrastructure.orm.db.news.model import News as _model


class NewsRepository:
    def get_availables(self) -> _t.List[_entity]:
        return list(map(lambda certs: _entity(**certs), _model.objects.values()))
