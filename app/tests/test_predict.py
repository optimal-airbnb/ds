from fastapi.testclient import TestClient
import sys
sys.path.append("./")
from app.main import app

client = TestClient(app)


def test_predict():
    """Return 200 Success when input returns valid json response."""
    response = client.post("/predict", json={
  "Borough": "Brooklyn",
  "Neighbourhood": "Clinton Hill",
  "Room_type": "Private room",
  "Minimum_nights": 1,
  "Availability_365": 365
})  
    assert response.status_code == 200
    assert response.json() == {"predicted_price ": '$232.42'}

test_predict()
# python app\tests\test_predict.py -v
# run the above line when ready