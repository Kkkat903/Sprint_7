import requests
import allure
from urls import Url as U
from data import Flags as F
import pytest
from data import ResponseMassages as R


class TestLogin:

    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверяет, что зарегистрированный курьер может авторизоваться с корректными логином и паролем. В ответе должен присутствовать ID курьера.")
    def test_courier_login_success(self, registered_courier):

        with allure.step("Подготовить данные для авторизации"):
            login_data = {
                "login": registered_courier["login"],
                "password": registered_courier["password"]
            }

        with allure.step("Отправить запрос на авторизацию курьера"):
            response = requests.post(
                f'{U.BASE_URL}{U.COURIER_LOGIN}',
                json=login_data
            )

        with allure.step("Проверить успешный статус ответа 200"):
            assert response.status_code == 200

        with allure.step("Проверить наличие ID курьера в ответе"):
            assert F.COURIER_ID in response.json()

    @allure.title("Авторизация без обязательного поля")
    @allure.description("Проверяет, что API возвращает ошибку 400, если при авторизации не передан логин или пароль.")
    @pytest.mark.parametrize('missing_field', ["login", "password"])
    def test_login_without_required_fields(self, courier_data_with_cleanup, missing_field):

        with allure.step("Создать нового курьера"):
            response = requests.post(
                f'{U.BASE_URL}{U.CREATE_COURIER}',
                json=courier_data_with_cleanup
            )
            assert response.status_code == 201

        with allure.step("Подготовить данные для авторизации без обязательного поля"):
            login_data = {
                "login": courier_data_with_cleanup["login"],
                "password": courier_data_with_cleanup["password"]
            }
            del login_data[missing_field]

        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(
                f'{U.BASE_URL}{U.COURIER_LOGIN}',
                json=login_data
            )

        with allure.step("Проверить статус ответа 400"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение об отсутствии обязательных данных"):
            assert response.json() == R.MISSING_REQUIRED_FIELDS_LOGIN

    @allure.title("Авторизация с некорректными данными")
    @allure.description("Проверяет, что API возвращает ошибку 404, если логин или пароль зарегистрированного курьера указаны неверно.")
    @pytest.mark.parametrize("wrong_field", ['login', 'password'])
    def test_login_with_wrong_field(self, courier_data_with_cleanup, wrong_field):

        with allure.step("Создать нового курьера"):
            response = requests.post(
                f'{U.BASE_URL}{U.CREATE_COURIER}',
                json=courier_data_with_cleanup
            )
            assert response.status_code == 201

        with allure.step("Подготовить данные с некорректным значением"):
            login_data = {
                "login": courier_data_with_cleanup["login"],
                "password": courier_data_with_cleanup["password"]
            }
            login_data[wrong_field] = login_data[wrong_field] + "wrong"

        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(
                f'{U.BASE_URL}{U.COURIER_LOGIN}',
                json=login_data
            )

        with allure.step("Проверить статус ответа 404"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение об отсутствии учетной записи"):
            assert response.json() == R.ERROR_ACCOUNT_NOT_FOUND

    @allure.title("Авторизация несуществующего курьера")
    @allure.description("Проверяет, что API возвращает ошибку 404 при попытке авторизации курьера, который предварительно не был зарегистрирован.")
    def test_login_nonexistent_user(self, courier_data_with_cleanup):

        with allure.step("Подготовить данные несуществующего курьера"):
            login_data = {
                "login": courier_data_with_cleanup["login"],
                "password": courier_data_with_cleanup["password"]
            }

        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(
                f'{U.BASE_URL}{U.COURIER_LOGIN}',
                json=login_data
            )

        with allure.step("Проверить статус ответа 404"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение об отсутствии учетной записи"):
            assert response.json() == R.ERROR_ACCOUNT_NOT_FOUND