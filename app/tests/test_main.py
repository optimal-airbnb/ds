from fastapi.testclient import TestClient
import sys
sys.path.append("./")
from app.main import app

client = TestClient(app)


def test_docs():
    """Just tests for a 200 code"""
    response = client.get("/")
    assert response.status_code == 200

test_docs()
# python app\tests\test_main.py -v
# run the above line when ready