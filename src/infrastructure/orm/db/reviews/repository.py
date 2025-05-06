# coding: utf-8

import typing as _t

from src.domain.entities.repositories import ReviewEntity as _entity
from src.infrastructure.orm.db.reviews.model import Review as _model


class ReviewRepository:
    def get_availables(self) -> _t.List[_entity]:
        return list(map(lambda reviews: _entity(**reviews), _model.objects.values()))
