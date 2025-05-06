# coding: utf-8

import typing as _t

from src.domain.entities.repositories import PopularEntity as _entity
from src.infrastructure.orm.db.populars.model import Popular as _model


class PopularRepository:
    def get_availables(self) -> _t.List[_entity]:
        return list(map(lambda partners: _entity(**partners), _model.objects.values()))
