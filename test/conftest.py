import random
import pytest
import requests
import string
import data

@pytest.fixture()
def register_new_courier_and_return_login_password():
    """ создание нового курьера и внесение в список его данных """
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

@pytest.fixture()
def courier_authorization(register_new_courier_and_return_login_password):
    """ авторизация курьера после его создания """
    payload = {"login": register_new_courier_and_return_login_password[0],
               "password": register_new_courier_and_return_login_password[1]}
    response = requests.post(data.url_courier_authorization, data=payload)
    return response

