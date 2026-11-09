from faker import Faker
import allure
import uuid

fake = Faker()

def login_generator():
    generated_login = f"{fake.user_name()}_{uuid.uuid4().hex[:8]}"
    return generated_login

def password_generator():
    generated_password = fake.password()
    return generated_password

def first_name_generator():
    generated_first_name = fake.first_name()
    return generated_first_name