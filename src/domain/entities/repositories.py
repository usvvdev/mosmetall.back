# coding: utf-8

import typing as _t
from urllib.parse import urljoin
from django.conf import settings
from pydantic import field_validator as _validator
from pydantic import ConfigDict as _config, BaseModel as _BM
from phonenumber_field import phonenumber
from datetime import datetime as _dt

from src.domain.core.constants import FILTER_PARAMS


class _Base(_BM):
    id: int
    model_config = _config(from_attributes=True)


class ImageMixin(_Base):
    image: str

    @_validator("image")
    @classmethod
    def construct_image_url(cls, value: str):
        return urljoin(settings.MEDIA_URL, value)


class FileMixin(_Base):
    file: str

    @_validator("file")
    @classmethod
    def construct_file_url(cls, value: str):
        return urljoin(settings.MEDIA_URL, value)


"""
### <-- BASE ENTITTIES FOR USING IN OTHER SHEMAS --> ### 
"""


class SectionsEntity(_Base):
    name: str


class ItemEntity(_Base):
    name: str
    type: _t.Optional[str] = None
    stamp: _t.Optional[str] = None
    gost: _t.Optional[str] = None
    size: _t.Optional[str] = None
    diameter: _t.Optional[str] = None
    length: _t.Optional[str] = None
    width: _t.Optional[str] = None
    thickness: _t.Optional[str] = None
    side: _t.Optional[str] = None
    nominal_diameter: _t.Optional[str] = None
    nominal_pressure: _t.Optional[str] = None
    material: _t.Optional[str] = None


class ProductEntity(ImageMixin):
    name: str
    size: str


class CategoriesEntity(_Base):
    name: str
    sections: _t.List["SectionsEntity"]

    @staticmethod
    def to_string(categories: "CategoriesEntity") -> str:
        sections = ", ".join([section.name for section in categories.sections.all()])
        return f"{categories.name} -> {sections}"


class Filters(_BM):
    name: _t.List
    type: _t.List
    stamp: _t.List
    gost: _t.List
    size: _t.List
    diameter: _t.List
    length: _t.List
    width: _t.List
    thickness: _t.List
    side: _t.List
    nominal_diameter: _t.List
    nominal_pressure: _t.List
    material: _t.List


"""
### <-- ----------------------------------------- --> ### 
"""


class ProjectEntity(ImageMixin):
    title: str
    location: str

    @staticmethod
    def to_string(project: "ProjectEntity") -> str:
        return f"{project.title} -> {project.location}"


class ReviewEntity(ImageMixin):
    author: str
    post: str
    description: str

    @staticmethod
    def to_string(review: "ReviewEntity") -> str:
        return f"{review.author} -> {review.post} : {review.description}"


class CertEntity(FileMixin):
    title: str
    type: str

    @staticmethod
    def to_string(cert: "CertEntity") -> str:
        return f"{cert.title} -> {cert.file}"


class PartnerEntity(ImageMixin):
    name: str

    @staticmethod
    def to_string(partner: "PartnerEntity") -> str:
        return f"{partner.id} -> {partner.image}"


class NewsEntity(ImageMixin):
    title: str
    description: str
    type: str
    link: str
    date: _dt

    @_validator("date")
    def construct_date(cls, value: str) -> str:
        return _dt.strptime(str(value), "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%y")

    @staticmethod
    def to_string(news: "NewsEntity") -> str:
        return f"{news.title} -> {news.description}: {news.link}"


class PopularEntity(ImageMixin):
    name: str

    @staticmethod
    def to_string(popular: "PopularEntity") -> str:
        return f"{popular.name} -> {popular.image}"


class ServicesEntity(_Base):
    name: str

    @staticmethod
    def to_string(service: "ServicesEntity") -> str:
        return f"{service.id} -> {service.name}"


class ServiceEntity(ServicesEntity, ImageMixin):
    subtitle: str
    description: str
    quote: str
    type: str
    size: str
    products: _t.List["ProductEntity"]

    @staticmethod
    def to_string(service: "ServiceEntity") -> str:
        return f"{service.name} -> {service.products}"


class SearchEntity(_BM):
    items: _t.List["ItemEntity"]
    current_page: _t.Optional[int] = None
    total_items: _t.Optional[int] = None
    filters: _t.Optional["Filters"] = None

    def set_filters(self):
        self.filters = Filters(
            **{
                attr: list(
                    {
                        getattr(item, attr)
                        for item in self.items
                        if getattr(item, attr) is not None
                    }
                )
                for attr in FILTER_PARAMS
            }
        )


class SectionEntity(SectionsEntity):
    items: _t.List["ItemEntity"]
    current_page: _t.Optional[int] = None
    total_items: _t.Optional[int] = None
    filters: _t.Optional["Filters"] = None

    @staticmethod
    def to_string(section: "SectionEntity") -> str:
        return f"{section.id} -> {section.name}"

    def set_filters(self):
        self.filters = Filters(
            **{
                attr: list(
                    {
                        getattr(item, attr)
                        for item in self.items
                        if getattr(item, attr) is not None
                    }
                )
                for attr in FILTER_PARAMS
            }
        )


class CategoryEntity(_Base):
    sections: _t.List["SectionsEntity"]

    @staticmethod
    def to_string(category: "CategoryEntity") -> str:
        return f"{category.id} -> {category.sections}"


class CatalogEntity(_Base):
    categories: _t.List["CategoriesEntity"]

    @staticmethod
    def to_string(catalog: "CatalogEntity") -> str:
        categories = ", ".join([category.name for category in catalog.categories.all()])
        return f"{catalog.id} -> {categories}"


class FormEntity(_BM):
    name: str
    email: _t.Optional[str] = None
    phone: str
    files: _t.Optional[_t.Any] = None
    page_title: str
    product_title: _t.Optional[str] = None

    @_validator("name", "email", "phone", "page_title", "product_title", mode="before")
    def ensure_string(cls, v):
        if isinstance(v, list):
            return v[0] if v else None
        return v
