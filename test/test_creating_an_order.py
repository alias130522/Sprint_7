import json
import pytest
import requests
import allure
import data


class TestCreatingAnOrder:
    @allure.title('Успешное создание заказа')
    @allure.description("Создание заказа с изменением цвета самоката")
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])
    def test_true_creating_an_order(self, color):
        data.data_order["color"] = color
        payload = data.data_order
        response = requests.post(data.url_creating_an_order, data=json.dumps(payload))
        assert response.status_code == 201 and "track" in response.text

