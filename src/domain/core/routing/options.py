# coding: utf-8

import typing as _t
from dataclasses import dataclass

from src.domain.core.constants import HTTP_VERBS


@dataclass
class Route:
    http_verb: str
    path: str
    controller: _t.Callable
    method: str
    name: str

    def __post_init__(self):
        has_method = hasattr(self.controller, self.method)
        assert has_method, f"Invalid method {self.method} for {self.controller}"
        assert self.http_verb in HTTP_VERBS, f"Invalid http verb {self.http_verb}"

    @property
    def url(self) -> str:
        return self.path

    @property
    def mapping(self) -> dict:
        return {self.http_verb: self.method}
