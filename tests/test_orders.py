import pytest
import requests
from urls import Url as U
import allure
from data import Data as D

class TestOrders:
    @allure.title("Создание заказа с разными вариантами цвета")
    @allure.description("Проверяет создание заказа с четырьмя вариантами цвета: GREY,BLACK, GREY и BLACK, без цвета.")
    @pytest.mark.parametrize("order_data", [D.ORDER_DATA_GREY, D.ORDER_DATA_BLACK, D.ORDER_DATA_BOTH, D.ORDER_DATA_NO_COLOR])

    def test_create_order_with_different_colors(self, order_data):

        with allure.step("Отправить POST-запрос на создание заказа"):
            response = requests.post(
                f'{U.BASE_URL}{U.CREATE_ORDER}',
                json=order_data
            )

        with allure.step("Проверить статус ответа 201"):
            assert response.status_code == 201
            
        with allure.step("Проверить наличие номера заказа track"):
            assert "track" in response.json()