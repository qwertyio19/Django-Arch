import pytest
from rest_framework.test import APIClient
from apps.news.models import News


@pytest.fixture
def api_client():
    """
    Клиент DRF для вызова API.
    Можешь потом расширить: авторизация, токены и т.д.
    """
    return APIClient()


@pytest.fixture
def news_factory():
    """
    Фабрика для создания объектов News.
    Позволяет переопределять поля по необходимости.
    """
    def factory(**kwargs):
        defaults = {
            "name": "Test news",
            "description": "Some description",
            "date": "2025-01-01",
            # Для ImageField достаточно строки — это путь в базе.
            "image": "news/images/test.jpg",
        }
        defaults.update(kwargs)
        return News.objects.create(**defaults)

    return factory
