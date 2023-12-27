import datetime
import random
import requests
import string
import random as r


def register_new_courier_and_return_login_password():
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


def register_new_courier(base_url, random_login, random_pass, random_name):
    """ создание нового курьера """
    payload = {"login": random_login, "password": random_pass, "firstName": random_name}
    response = requests.post(base_url, data=payload)
    return response

def generating_data_day():
    data_day = str(datetime.date.today())
    return data_day

def generating_telefon_namber():
    telefon = str(''.join(map(str, random.sample(range(10),9))))
    namber = '+79'+ telefon
    return namber


