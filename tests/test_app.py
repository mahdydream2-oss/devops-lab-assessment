import pytest

from app.main import app, validate_item, _items


@pytest.fixture
def client():
    _items.clear()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_valid_item_passes_validation():
    assert validate_item({"found_at": "محطة الحافلات", "category": "wallet"}) == []


def test_short_location_is_rejected():
    assert validate_item({"found_at": "a", "category": "keys"})


def test_unknown_category_is_rejected():
    assert validate_item({"found_at": "محطة الحافلات", "category": "laptop"})


def test_create_and_list_item(client):
    r = client.post("/api/items", json={"found_at": "محطة الحافلات", "category": "phone"})
    assert r.status_code == 201
    assert client.get("/api/items").get_json()[0]["id"] == 1


def test_invalid_item_returns_400(client):
    r = client.post("/api/items", json={"found_at": ""})
    assert r.status_code == 400
