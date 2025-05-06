# coding: utf-8

from src.domain.core.constants import HTTP_VERB_GET
from src.domain.core.routing.router import Router
from src.domain.core.routing.options import Route
from src.interface.routes.constants import CATALOG_PREFIX, SEARCH_PREFIX
from src.interface.controllers.catalogs.controller import (
    CatalogController as _controller,
)


catalog_router = Router()
catalog_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{CATALOG_PREFIX}",
            controller=_controller,
            method="list",
            name="catalog_list",
        ),
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{CATALOG_PREFIX}/(?P<category_id>[a-zA-Z0-9_]+)",
            controller=_controller,
            method="get_category",
            name="category_get",
        ),
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{CATALOG_PREFIX}/(?P<category_id>[a-zA-Z0-9_]+)/(?P<section_id>[a-zA-Z0-9_]+)",
            controller=_controller,
            method="get_section",
            name="section_get",
        ),
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{SEARCH_PREFIX}",
            controller=_controller,
            method="search_items",
            name="search_item",
        ),
    ]
)
