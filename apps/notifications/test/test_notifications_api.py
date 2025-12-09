# apps/notifications/test/test_notifications_api.py
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_type_notification_list_empty(api_client):
    """
    Если в БД нет типов уведомлений, API должно вернуть пустой список.
    """
    url = reverse("type-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_type_notification_list_with_items(api_client, type_notification_factory):
    """
    Список типов уведомлений должен возвращать все объекты с нужными полями.
    """
    type1 = type_notification_factory(type="Объявление")
    type2 = type_notification_factory(type="Сообщение")

    url = reverse("type-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2

    first_item = response.data[0]
    assert "id" in first_item
    assert "type" in first_item

    returned_types = {item["type"] for item in response.data}
    assert {"Объявление", "Сообщение"} <= returned_types


@pytest.mark.django_db
def test_type_notification_detail(api_client, type_notification_factory):
    """
    Детальный просмотр типа уведомления.
    """
    type_obj = type_notification_factory(type="Важно")

    url = reverse("type-detail", args=[type_obj.id])
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.data
    assert data["id"] == type_obj.id
    assert data["type"] == "Важно"


@pytest.mark.django_db
def test_type_notification_detail_not_found(api_client):
    """
    Если типа уведомления не существует — 404.
    """
    url = reverse("type-detail", args=[99999])
    response = api_client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_notification_list_with_nested_type(api_client, notification_factory):
    """
    Список уведомлений должен возвращать вложенный объект types
    с полями id и type.
    """
    notification = notification_factory()  # c дефолтным типом

    url = reverse("notification-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1

    item = response.data[0]

    # Проверяем основные поля
    for field in ("id", "types", "title", "description", "date", "image"):
        assert field in item

    # Проверяем nested-сериализатор types
    types_data = item["types"]
    assert isinstance(types_data, dict)
    assert "id" in types_data
    assert "type" in types_data
    assert types_data["id"] == notification.types.id
    assert types_data["type"] == notification.types.type


@pytest.mark.django_db
def test_notification_detail(api_client, notification_factory):
    """
    Детальный просмотр уведомления, вместе с вложенным типом.
    """
    notification = notification_factory(
        title="Скидки на обучение",
        date="2025-02-01",
    )

    url = reverse("notification-detail", args=[notification.id])
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.data

    assert data["id"] == notification.id
    assert data["title"] == "Скидки на обучение"
    assert data["date"] == "2025-02-01"

    # nested types
    assert "types" in data
    assert data["types"]["id"] == notification.types.id
    assert data["types"]["type"] == notification.types.type


@pytest.mark.django_db
def test_notification_detail_not_found(api_client):
    """
    Если уведомления с таким id нет — 404.
    """
    url = reverse("notification-detail", args=[99999])
    response = api_client.get(url)

    assert response.status_code == 404
