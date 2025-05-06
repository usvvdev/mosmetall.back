# coding: utf-8

import typing as _t

from src.domain.entities.repositories import CertEntity as _entity
from src.infrastructure.orm.db.certs.model import Cert as _model


class CertRepository:
    def get_availables(self) -> _t.List[_entity]:
        return list(map(lambda certs: _entity(**certs), _model.objects.values()))
