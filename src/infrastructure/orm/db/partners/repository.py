# coding: utf-8

import typing as _t

from src.domain.entities.repositories import PartnerEntity as _entity
from src.infrastructure.orm.db.partners.model import Partner as _model


class PartnerRepository:
    def get_availables(self) -> _t.List[_entity]:
        return list(map(lambda partners: _entity(**partners), _model.objects.values()))
