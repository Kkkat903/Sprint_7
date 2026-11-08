import pytest
import generators
import allure
from urls import Url as U
import requests

@pytest.fixture
@allure.title("Генерация данных курьера")
@allure.description("Создаёт уникальные тестовые данные курьера: логин, пароль и имя.")
def generate_courier_data():
    courier_data = {
        "login": generators.login_generator(),
        "password": generators.password_generator(),
        "firstName": generators.first_name_generator()
    }
    return courier_data

@pytest.fixture
def courier_data_with_cleanup(generate_courier_data):
    original_data = generate_courier_data.copy()

    yield generate_courier_data

    login_data = {
        "login": original_data["login"],
        "password": original_data["password"]
    }

    login_response = requests.post(
        f'{U.BASE_URL}{U.COURIER_LOGIN}',
        json=login_data
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]

        requests.delete(
            f'{U.BASE_URL}{U.DELETE_COURIER}{courier_id}'
        )
        
@pytest.fixture
@allure.title("Cоздание курьера")
@allure.description("Регистрирует курьера с уникальными данными")
def registered_courier(courier_data_with_cleanup):
    response = requests.post(
        f'{U.BASE_URL}{U.CREATE_COURIER}',
        json=courier_data_with_cleanup
    )

    assert response.status_code == 201

    return courier_data_with_cleanup