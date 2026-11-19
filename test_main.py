
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_student():
    response = client.post(
        "/students",
        json={
            "roll_no": 101,
            "name": "Sneha",
            "age": 22,
            "course": "MCA"
        }
    )
    assert response.status_code == 200


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200


def test_get_student():
    response = client.get("/students/101")
    assert response.status_code == 200


def test_delete_student():
    response = client.delete("/students/101")
    assert response.status_code == 200


def test_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404

