from app import app
def test_total_and_average():
    response = app.test_client().post("/", data={"marks": "80,90,70" })
    assert response.status_code == 200
    assert b"Total: 240" in response.data
    assert b"Average: 80.00" in response.data
def test_invalid_marks():
    response = app.test_client().post("/", data={"marks": "120,50"})
    assert b"valid marks between 0 and 100" in response.data
def test_health():
     assert app.test_client().get("/health").json["status"] == "healthy"
