import pytest
import generators
import allure

@pytest.fixture
@allure.title("Генерация данных курьера")
@allure.description("Создаёт уникальные тестовые данные курьера: логин, пароль и имя.")
def generate_courier_data():
    courier_data = {
        "login": generators.login_generator(),
        "password": generators.password_generator(),
        "firstName": generators.first_name_generator()
    }
    yield courier_data