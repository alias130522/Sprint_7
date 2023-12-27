import json
import pytest
import requests

from data import data_creating_an_order


class TestCreatingAnOrder:

    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])
    def test_true_creating_an_order(self, color, random_name):
        url = 'http://qa-scooter.praktikum-services.ru/api/v1/orders'
        data_creating_an_order.data_order["color"] = color
        payload = data_creating_an_order.data_order
        response = requests.post(url, data=json.dumps(payload))
        print(payload)
        assert response.status_code == 201