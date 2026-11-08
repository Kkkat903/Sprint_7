import requests
import allure
from urls import Url as U
from data import ResponseMassages as R
import pytest


class TestCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Проверяет, что курьер успешно создаётся с корректными данными.Ожидаемый статус ответа — 201, тело ответа — {'ok': True}.")
    def test_create_courier(self, courier_data_with_cleanup):

        with allure.step("Отправить POST-запрос на создание курьера"):
            response = requests.post(
                f'{U.BASE_URL}{U.CREATE_COURIER}',
                json=courier_data_with_cleanup
            )

        with allure.step("Проверить статус ответа 201"):
            assert response.status_code == 201

        with allure.step("Проверить тело ответа об успешном создании"):
            assert response.json() == R.CREATE_COURIER_SUCCESS

    @allure.title("Создание курьера с уже существующим логином")
    @allure.description("Проверяет, что API не позволяет создать двух курьеров с одинаковым логином и возвращает ошибку 409.")
    def test_create_courier_duplicate_login_shows_error(self, courier_data_with_cleanup):

        with allure.step("Создать первого курьера"):
            requests.post(
                 f'{U.BASE_URL}{U.CREATE_COURIER}',
                 json=courier_data_with_cleanup
                 )

        with allure.step("Повторно отправить запрос с теми же данными"):
            response = requests.post(
                f'{U.BASE_URL}{U.CREATE_COURIER}',
                json=courier_data_with_cleanup
            )

        with allure.step("Проверить статус ошибки 409 при повторном создании"):
            assert response.status_code == 409

        with allure.step("Проверить сообщение об уже существующем логине"):
            assert response.json() == R.ERROR_DUPLICATE_LOGIN

    @allure.title("Создание курьера без обязательного поля")
    @allure.description("Проверяет, что API возвращает ошибку 400, если при создании курьера не передано одно из обязательных полей: login, password или firstName.")
    @pytest.mark.parametrize("missing_field", ['login', 'password', 'firstName'])
    def test_create_courier_without_required_fields(self, courier_data_with_cleanup, missing_field):

        with allure.step("Удалить обязательное поле из данных курьера"):
            del courier_data_with_cleanup[missing_field]

        with allure.step("Отправить POST-запрос на создание курьера"):
            response = requests.post(
                f'{U.BASE_URL}{U.CREATE_COURIER}',
                json=courier_data_with_cleanup
            )

        with allure.step("Проверить статус ответа 400"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение об отсутствии обязательных данных"):
            assert response.json() == R.MISSING_REQUIRED_FIELDS