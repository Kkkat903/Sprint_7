import pytest
import requests
from urls import Url as U
from data import Colors as C
import allure

class TestOrders:
    @allure.title("Создание заказа с разными вариантами цвета")
    @allure.description("Проверяет создание заказа с четырьмя вариантами цвета: GREY,BLACK, GREY и BLACK, без цвета.")
    @pytest.mark.parametrize("color", C.ORDER_COLORS)
    def test_create_order_with_different_colors(self, color):
        order_data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2026-11-10",
            "comment": "Saske, come back to Konoha"
        }
        with allure.step("Подготовить данные для создания заказа"):
            if color is not None:
                order_data["color"] = color

        with allure.step("Отправить POST-запрос на создание заказа"):
            response = requests.post(
                f'{U.BASE_URL}{U.CREATE_ORDER}',
                json=order_data
            )
        with allure.step("Проверить статус ответа 201"):
            assert response.status_code == 201
            
        with allure.step("Проверить наличие номера заказа track"):
            assert "track" in response.json()