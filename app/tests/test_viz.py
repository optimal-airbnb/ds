from fastapi.testclient import TestClient
import sys
sys.path.append("./")
from app.main import app

client = TestClient(app)


def test_viz():
    """Return 200 Success if response is fig.json file"""
    response = client.get("/map")
    assert response.status_code == 200
    assert isinstance(response, object)

test_viz()
# python app\tests\test_viz.py -v
# run the above line
