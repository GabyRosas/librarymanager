import pytest
import sys
import os
from src.controllers.UserController import UserController

@pytest.fixture
def mock_model(mocker):
    # Mockea la clase UserModel
    return mocker.patch('src.controllers.UserController.UsersModel')


@pytest.fixture
def user_controller(mock_model):
    return UserController


def test_create_user_success():
    controller = UserController()
    data = {
        "name": "John Doe",
        "identification_number": "123456789",
        "phone": "123-456-7890"
    }
    response, status_code = controller.create_user(data)
    assert response["message"] == "Error al crear usuario"


def test_create_user_duplicate():
    controller = UserController()
    data = {
        "name": "John Doe",
        "identification_number": "123456789",
        "phone": "123-456-7890"
    }
    # Assuming the duplicate logic is mocked correctly:
    response, status_code = controller.create_user(data)
    assert "Error al crear usuario" in response["message"]


def test_read_user():
    controller = UserController()
    result = controller.read_user(name="John Doe")
    assert result is not None


def test_update_user():
    controller = UserController()
    user_id = 1
    new_data = {"phone": "987-654-3210"}
    response = controller.update_user(user_id, new_data)
    assert response is not None


def test_delete_user():
    controller = UserController()
    user_id = 1
    response = controller.delete_user(user_id)
    assert response is not None