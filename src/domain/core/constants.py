# coding: utf-8

###<-- PROJECT APPS -->###

PROJECT_APPS = (
    "projects",
    "reviews",
    "certs",
    "partners",
    "news",
    "populars",
    "services",
    "catalogs",
    "forms",
)

###<-- ALLOWED FILE TYPES -->###

FILE_TYPE = ("pdf", "png", "jpeg", "jpg", "webp", "avif")
EXTENSION_FILE_TYPES = {
    "pdf": "pdf",
    **{value: "image" for value in FILE_TYPE},
}

###<-- ALLOWED HTTPS VERBS -->###
HTTP_VERB_DELETE = "delete"
HTTP_VERB_GET = "get"
HTTP_VERB_PATCH = "pacth"
HTTP_VERB_POST = "post"
HTTP_VERB_PUT = "put"

###<-- LIST OF HTTPS VERBS -->###
HTTP_VERBS = {
    HTTP_VERB_DELETE,
    HTTP_VERB_GET,
    HTTP_VERB_PATCH,
    HTTP_VERB_POST,
    HTTP_VERB_PUT,
}

###<-- LIST OF FILTER PARAMS -->###

FILTER_PARAMS = (
    "name",
    "type",
    "stamp",
    "gost",
    "size",
    "diameter",
    "length",
    "width",
    "thickness",
    "side",
    "nominal_diameter",
    "nominal_pressure",
    "material",
)


###<-- EMAIL MESSAGE TEMPLATE -->###

EMAIL_MESSAGE = """
Вам пришла заявка с сайта - mosmetall.group, со страницы {page_title}{product_line}
Имя клиента – {name}
Телефон клиента – {phone}
{email_line}
"""
