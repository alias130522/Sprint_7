import random

import pytest
import requests
import string

import helpers


#from helpers import Courier


@pytest.fixture()
def random_name():
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(8))
    actual_name = name
    return actual_name

@pytest.fixture()
def random_pass():
    """Метод генерирует рандомный пароль из букв латинского алфавита и цифр"""
    password = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    actual_password = password
    return actual_password

@pytest.fixture()
def random_login():
    """Метод генерирует рандомное login из букв латинского алфавита."""
    login = (f"{''.join(random.choice(string.ascii_uppercase) for i in range(1))}"
            f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}")
    actual_login = login
    return actual_login

@pytest.fixture()
def base_url():
    base_url = 'http://qa-scooter.praktikum-services.ru/api/v1/courier'
    return base_url

@pytest.fixture()
def register_new_courier(base_url, random_login, random_pass, random_name):
    """ создание нового курьера """
    payload = {"login": random_login, "password": random_pass, "firstName": random_name}
    response = requests.post(base_url, data=payload)
    return response
