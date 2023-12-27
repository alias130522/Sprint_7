import pytest
import requests
import json
import helpers

from conftest import random_login, random_pass


class TestLoginCourier:

    def test_true_courier_authorization(self, register_new_courier, random_login, random_pass):
        """ успешная авторизация курьера """
        url = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": random_login, "password": random_pass}
        response = requests.post(url, data=payload)
        print(response.text)
        assert response.status_code == 200

    def test_true_courier_authorization_and_return_id(self, register_new_courier, random_login, random_pass):
        """ успешная авторизация курьера с указанием  id """
        url = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": random_login, "password": random_pass}
        response = requests.post(url, data=payload)
        print(response.text)
        assert "id" in response.text

    def test_courier_authorization_not_login(self, register_new_courier, random_pass):
        """ проверка авторизации курьера без указания login """
        url = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"password": random_pass}
        response = requests.post(url, data=payload)
        print(payload)
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    def test_courier_authorization_not_password(self, register_new_courier, random_login):
        """ проверка авторизации курьера без указания password """
        url = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": random_login}
        response = requests.post(url, data=payload)
        print(payload)
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @pytest.mark.parametrize('wrong_data', [
                                                {"login": helpers.register_new_courier_and_return_login_password()[1], "password": 'wrong_pass'},
                                                {"login": 'wrong_login', "password": helpers.register_new_courier_and_return_login_password()[2]},
                                                {"login": 'wrong_login', "password": 'wrong_pass'}])
    def test_courier_authorization_wrong_(self, wrong_data):
        """ проверка авторизации курьера с неверным логином, паролем, парой догин-пароль"""
        helpers.register_new_courier_and_return_login_password()
        url = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = wrong_data
        response = requests.post(url, data=payload)
        print(payload)
        assert response.status_code == 404


