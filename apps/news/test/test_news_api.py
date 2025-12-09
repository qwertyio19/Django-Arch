# apps/news/tests/test_news_api.py
import pytest
from django.urls import reverse

from apps.news.models import News


@pytest.mark.django_db
def test_news_list_empty(api_client):
    """
    Если в БД нет новостей, API должен вернуть пустой список.
    """
    url = reverse("news-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_news_list_returns_items(api_client, news_factory):
    """
    API /news/ должно возвращать список новостей с нужными полями.
    """
    news1 = news_factory(name="News 1", date="2024-01-01")
    news2 = news_factory(name="News 2", date="2024-02-01")

    url = reverse("news-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2

    # Проверяем, что нужные поля присутствуют
    first_item = response.data[0]
    for field in ("id", "name", "description", "image", "date"):
        assert field in first_item

    # Можно проверить порядок, если важно (обычно по id или date)
    returned_names = [item["name"] for item in response.data]
    assert "News 1" in returned_names
    assert "News 2" in returned_names


@pytest.mark.django_db
def test_news_detail(api_client, news_factory):
    """
    API /news/<id>/ должно возвращать конкретную новость.
    """
    news = news_factory(
        name="Detail News",
        description="Full description",
        date="2024-03-01",
        image="news/images/detail.jpg",
    )

    url = reverse("news-detail", args=[news.id])
    response = api_client.get(url)

    assert response.status_code == 200

    data = response.data
    assert data["id"] == news.id
    assert data["name"] == "Detail News"
    assert data["description"] == "Full description"
    assert data["date"] == "2024-03-01"

    # image обычно возвращается как путь или полный URL
    assert "detail.jpg" in data["image"]


@pytest.mark.django_db
def test_news_detail_not_found(api_client):
    """
    Если новости с таким id нет, должен быть 404.
    """
    url = reverse("news-detail", args=[99999])
    response = api_client.get(url)

    assert response.status_code == 404
