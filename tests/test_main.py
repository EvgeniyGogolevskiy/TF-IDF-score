def test_upload_page_loads(client):
    response = client.get("/upload")
    assert response.status_code == 200
    assert "Upload a Text File" in response.text


def test_file_upload_and_results(client):
    file_content = b"hello world\nhello Lesta Games\nworld hello"
    files = {"file": ("testfile.txt", file_content, "text/plain")}

    response = client.post("/upload", files=files)

    assert response.status_code == 200
    assert "hello" in response.text
    assert "world" in response.text
    assert "lesta" in response.text.lower()
    assert "<table" in response.text
