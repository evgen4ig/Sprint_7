import pytest
import requests
import json
import allure
from urls import Urls
from endpoints import Endpoints
from data import OrderData


class TestCreateOrder:

    url = f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER_EP}'

    @allure.title('Успешное создание ордера со скутерами различных цветов')
    @pytest.mark.parametrize('color',
                             [
                                 ['BLACK'],
                                 ['GREY'],
                                 ['BLACK', 'GREY'],
                                 [],
                                 None
                             ],
                             ids=['black', 'grey', 'black&grey', '[]', 'None'])
    def test_create_order_with_different_colors_success(self, color):
        payload = OrderData.order_data
        payload['color'] = color
        with allure.step(f'Отправка запроса на создание ордера, цвет скутера - {color}'):
            response = requests.post(self.url, data=json.dumps(payload))

        assert (response.status_code == 201 and 'track' in response.json())