"""API tests with names matching the IBM Pictures capstone evidence tasks."""


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "OK"}


def test_count(client):
    response = client.get("/count")
    assert response.status_code == 200
    assert response.json["length"] == 10


def test_data_contains_10_pictures(client):
    response = client.get("/picture")
    assert len(response.json) == 10


def test_get_picture(client):
    response = client.get("/picture")
    assert response.status_code == 200
    assert len(response.json) == 10


def test_get_pictures_check_content_type_equals_json(client):
    response = client.get("/picture")
    assert response.headers["Content-Type"] == "application/json"


def test_get_picture_by_id(client):
    response = client.get("/picture/2")
    assert response.status_code == 200
    assert response.json["id"] == 2
    assert client.get("/picture/404").status_code == 404


def test_pictures_json_is_not_empty(client):
    assert len(client.get("/picture").json) > 0


def test_post_picture(client, picture):
    response = client.post("/picture", json=picture)
    assert response.status_code == 201
    assert response.json["id"] == 200
    assert client.get("/count").json["length"] == 11


def test_post_picture_duplicate(client, picture):
    client.post("/picture", json=picture)
    response = client.post("/picture", json=picture)
    assert response.status_code == 302
    assert response.json["Message"] == "picture with id 200 already present"


def test_update_picture_by_id(client):
    picture = client.get("/picture/2").json
    picture["event_state"] = "*" + picture["event_state"]
    response = client.put("/picture/2", json=picture)
    assert response.status_code == 200
    assert client.get("/picture/2").json["event_state"] == picture["event_state"]


def test_delete_picture_by_id(client):
    assert client.get("/count").json["length"] == 10
    response = client.delete("/picture/1")
    assert response.status_code == 204
    assert client.get("/count").json["length"] == 9
    assert client.delete("/picture/100").status_code == 404
