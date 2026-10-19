"""Fixtures for the independent Flask Pictures API tests."""
import json
from pathlib import Path

import pytest
from backend import app
from backend import routes


@pytest.fixture(autouse=True)
def restore_seed_data():
    """Ensure tests do not depend on execution order."""
    path = Path(__file__).resolve().parents[1] / "backend" / "data" / "pictures.json"
    routes.data[:] = json.loads(path.read_text(encoding="utf-8"))
    yield


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    return app.test_client()


@pytest.fixture()
def picture():
    return {
        "id": 200,
        "pic_url": "https://picsum.photos/seed/ibm-new-event/300/200",
        "event_country": "United States",
        "event_state": "California",
        "event_city": "Fremont",
        "event_date": "11/2/2030",
    }
