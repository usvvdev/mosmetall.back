# coding: utf-8

import typing as _t

from src.domain.entities.repositories import ProjectEntity as _entity
from src.infrastructure.orm.db.projects.model import Project as _model


class ProjectsRepository:
    def get_availables(self) -> _t.List[_entity]:
        return list(map(lambda projects: _entity(**projects), _model.objects.values()))
