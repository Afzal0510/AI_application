from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_upload_pdf():
    response = client.post("/upload_pdf/", files={"file": ("example.pdf", b"PDF content")})
    assert response.status_code == 200

def test_ask_question():
    response = client.post("/ask_question/", json={"question": "What is this PDF about?"})
    assert response.status_code == 200
