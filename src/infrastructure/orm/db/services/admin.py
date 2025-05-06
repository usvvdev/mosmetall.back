# coding: utf-8

from django.contrib import admin as _a

from src.infrastructure.adminsite.services.admin import (
    ServiceAdmin as _service_a,
    ProductAdmin as _product_a,
)
from src.infrastructure.orm.db.services.model import (
    Product as _product,
    Service as _service,
)

[
    _a.site.register(model, admin)
    for model, admin in ((_service, _service_a), (_product, _product_a))
]
