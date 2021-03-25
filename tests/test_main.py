from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_app():
    response = client.get("/api/badge/")
    assert response.status_code == 200
    assert response.json() == {
        "schemaVersion": 1,
        "label": "",
        "message": "live",
        "color": "#7673C0",
        "labelColor": "#430098",
        "namedLogo": "heroku",
        "style": "for-the-badge",
        "cacheSeconds": 500
    }