# import pytest
# from dirty_equals import IsDict
from fastapi.testclient import TestClient


from src.main import backend_app

client = TestClient(backend_app)

# @pytest.mark.parametrize(
#     "path,expected_status,expected_response",
#     [
#         ("/api_route", 200, {"message": "alive"}),
#         ("/non_decorated_route", 200, {"message": "Hello World"}),
#         ("/nonexistent", 404, {"detail": "Not Found"}),
#     ],
# )
def test_health_check():
    response = client.get("/api/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "alive"}
    
def test_summarize_webpage_empty_request():
    test_empty_content = {}
    response = client.post("/api/summarize/webpage", json=test_empty_content)
    assert response.status_code == 422

def test_summarize_text_empty_request():
    test_empty_content = {}
    response = client.post("/api/summarize/text", json=test_empty_content)
    assert response.status_code == 422

def test_summarize_webpage():
    test_content = {"url": "https://medium.com/new-writers-welcome/dosa-hunt-in-toronto-25c204857e30", "summary_len":200}
    response = client.post("/api/summarize/webpage", json=test_content)
    assert response.status_code == 200
    assert "summary" in response.json()
    
def test_summarize_text():
    text = """
    First things first, I grew up in Chennai — a South Indian city, which meant only one thing — we ate idly, dosa (a savory pancake made from fermented rice and dal batter) every day. Sometimes I’d try cheating my way around on the weekend with a roti/chapati, a chaat, rare luxury - a pizza, but dosa will find its way to my tummy. After a tired day filling my cravings up with multi-continental cuisines, I’d reach home to hear my mom yell,

“Suck up to the dosas on the table, they’ve been waiting for you all day!”

People, things, life in general came and went, but dosa stayed with me through thick and thin. Until I reached my teenage (after which I couldn’t afford to!) dosas solved most of my problems. I could keep eating, and I loved eating until nothing else mattered. Dosas were very forgiving too — If there was no sambar, chutney, or curry, no worries there’s podi, or pickle. You can only imagine my Indian mother’s terror-filled 30s having a fatso girl child.
    """
    test_content = {"text": text, "summary_len":200}
    response = client.post("/api/summarize/text", json=test_content)
    assert response.status_code == 200
    assert "summary" in response.json()