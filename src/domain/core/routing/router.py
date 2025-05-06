# coding: utf-8

import typing as _t

from src.domain.core.routing.options import Route


class Router:
    def __init__(self, name: str = None):
        self.name = name
        self.registry = dict()

    def register(self, routes: _t.Union[_t.Iterable, Route]):
        routes = routes if isinstance(routes, _t.Iterable) else [routes]
        for route in routes:
            name = f"{self.name}_{route.name}" if self.name else route.name
            assert name not in self.registry, f"{name} route already registered"
            self.registry.update({name: route})

    def get_route(self, name: str) -> Route:
        return self.registry.get(name) if name in self.registry else None

    def get_url(self, name: str) -> str:
        route = self.get_route(name)
        return route.url if route else None

    def get_urls(self) -> list:
        return [route.url for route in self.registry.values()]

    def map(self, name: str) -> dict:
        route = self.get_route(name)
        return route.mapping if route else None
