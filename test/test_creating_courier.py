import requests

class TestCreatingCourier:
    def test_can_create_courier(self, register_new_courier):
        """ можно создать курьера, возвращается верный код ответа """
        assert register_new_courier.status_code == 201

    def test_cannot_create_two_identical_couriers(self, base_url, random_login, random_pass, random_name):
        """ проверка невозможности создания двух одинаковых курьеров """
        payload = {"login": random_login, "password": random_pass, "firstName": random_name}
        requests.post(base_url, data=payload)
        pay = {"login": random_login, "password": random_pass, "firstName": random_name}
        response = requests.post(base_url, data=pay)
        assert response.status_code == 409

    def test_not_login_required_field(self, base_url, random_pass, random_name):
        """ проверка ответа при не заполнении одного из обязательных полей login """
        payload = {"password": random_pass, "firstName": random_name}
        response = requests.post(base_url, data=payload)
        assert response.status_code == 400

    def test_not_password_required_field(self, base_url, random_login, random_name):
        """ проверка ответа при не заполнении одного из обязательных полей password """
        payload = {"login": random_login, "firstName": random_name}
        response = requests.post(base_url, data=payload)
        assert response.status_code == 400

    def test_text_create_courier(self, register_new_courier):
        """ проверка текста ответа при успешном создании курьера """
        assert register_new_courier.text == '{"ok":true}'


