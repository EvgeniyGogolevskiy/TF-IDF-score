import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_upload_file_success():
    file_path = "tests/test_files/test.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Hello world! Hello Lesta!")

    with open(file_path, "rb") as file:
        response = client.post(
            "/upload",
            files={"file": ("test.txt", file, "text/plain")}
        )

    assert response.status_code == 200
    assert "Hello" in response.text or "hello" in response.text

    os.remove(file_path)


def test_upload_file_no_file():
    response = client.post("/upload", files={})

    assert response.status_code == 422


def test_get_upload_form():
    response = client.get("/upload")
    assert response.status_code == 200
    assert "<form" in response.text
