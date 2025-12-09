# apps/notifications/test/conftest.py
import pytest
from rest_framework.test import APIClient
from apps.notifications.models import TypeNotification, Notification


@pytest.fixture
def api_client():
    """
    DRF клиент для запросов в тестах.
    Если уже есть global api_client в корне проекта — можешь этот не создавать.
    """
    return APIClient()


@pytest.fixture
def type_notification_factory():
    """
    Фабрика типов уведомлений.
    """
    def factory(**kwargs):
        defaults = {
            "type": "Объявление",   # дефолтное название типа
        }
        defaults.update(kwargs)
        return TypeNotification.objects.create(**defaults)

    return factory


@pytest.fixture
def notification_factory(type_notification_factory):
    """
    Фабрика уведомлений.
    Если тип не передан, создаём дефолтный TypeNotification.
    """
    def factory(**kwargs):
        type_obj = kwargs.pop("types", None) or type_notification_factory()

        defaults = {
            "types": type_obj,
            "title": "Тестовая реклама",
            "description": "<p>Описание</p>",
            "date": "2025-01-01",
            "image": "notifications/test.jpg",  # как путь в БД
        }
        defaults.update(kwargs)
        return Notification.objects.create(**defaults)

    return factory
