import requests
import allure
from urls import Urls
from endpoints import Endpoints
from data import OrderData


class TestGetOrderList:

    url = f'{Urls.MAIN_URL}{Endpoints.GET_ORDER_LIST_EP}'

    @allure.title('Успешное получение списка ордеров')
    def test_get_order_list_success(self):

        params = OrderData.order_list_data
        with allure.step('Запрос на получение списка ордеров'):
            response = requests.get(self.url, params=params)

        assert (response.status_code == 200 and isinstance(response.json()['orders'], list))