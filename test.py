from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_endpoint():
    response = client.get("/api/search?airline_code=AK&airline_number=44&departure_date=2024-7-12")
    assert response.status_code == 200