import requests
from urls import Url as U
import allure

class TestOrdersList:

    @allure.title("Получение списка заказов")
    @allure.description("Проверяет получение списка заказов через GET-запрос. Проверяет успешный статус ответа 200 и то, что поле orders содержит список.")
    def test_get_orders_list(self):

        with allure.step("Отправить GET-запрос для получения списка заказов"):
            response = requests.get(f'{U.BASE_URL}{U.CREATE_ORDER}')

        with allure.step("Проверить статус ответа 200"):
            assert response.status_code == 200

        with allure.step("Проверить, что orders является списком"):
            assert isinstance(response.json()["orders"], list)