# coding: utf-8

import smtplib
from os import environ as _env
from email.message import EmailMessage as _message

from src.domain.entities.repositories import FormEntity as _entity
from src.domain.core.constants import EMAIL_MESSAGE as _email_message


class FormUtils:
    _login: str = _env.get("EMAIL_NAME")
    _password: str = _env.get("EMAIL_PASSWORD")
    _email_to: str = _env.get("EMAIL_TO")
    _smtp_server: str = "smtp.gmail.com"

    @classmethod
    def __set_content(cls, data: _entity) -> str:
        return _email_message.format(
            **data.__dict__,
            email_line=f"Почта клиента – {data.email}" if data.email else "",
            product_line=f", товар – {data.product_title}"
            if data.product_title
            else "",
        )

    @classmethod
    def __set_message(cls, data: _entity) -> _message:
        msg = _message()
        msg.set_content(cls.__set_content(data))
        msg["Subject"] = "Новая заявка"
        msg["From"] = cls._login
        msg["To"] = cls._email_to

        if data.files:
            for file in data.files:
                file_name = file.name
                file_data = file.read()
                msg.add_attachment(
                    file_data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_name,
                )
        return msg

    @classmethod
    def send_email(cls, data: dict):
        with smtplib.SMTP_SSL(cls._smtp_server, 465) as connection:
            connection.login(user=cls._login, password=cls._password)
            connection.send_message(cls.__set_message(_entity(**data)))
