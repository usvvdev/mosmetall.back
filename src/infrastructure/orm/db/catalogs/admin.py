# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.catalogs.admin import (
    CatalogAdmin as _catalog_a,
    CategoryAdmin as _category_a,
    SectionAdmin as _section_a,
    ItemAdmin as _item_a,
)
from src.infrastructure.orm.db.catalogs.model import (
    Catalog as _catalog,
    Category as _category,
    Section as _section,
    Item as _item,
)

[
    _a.site.register(model, admin)
    for model, admin in (
        (_catalog, _catalog_a),
        (_category, _category_a),
        (_section, _section_a),
        (_item, _item_a),
    )
]
