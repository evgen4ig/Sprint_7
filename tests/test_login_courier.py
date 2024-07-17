import pytest
import requests
import allure
from urls import Urls
from endpoints import Endpoints
from data import MessagesData, CourierData


class TestLoginCourier:

    url = f'{Urls.MAIN_URL}{Endpoints.LOGIN_COURIER_EP}'

    @allure.title('Успешная авторизация курьера')
    def test_log_in_courier_success(self, new_courier):
        with allure.step('Отправка запроса на авторизацию курьера'):
            response = requests.post(self.url, data=new_courier)

        assert (response.status_code == 200 and 'id' in response.json())


    @allure.title('Невозможность авторизоваться курьером без обязательного поля')
    @pytest.mark.parametrize('key, empty_field',
                             [
                                 ['login', CourierData.empty_log_in_data['login']],
                                 ['password', CourierData.empty_log_in_data['password']]
                             ],
                             ids=['without_login', 'without_password'])
    def test_log_in_courier_without_required_field_failure(self, key, empty_field, new_courier):
        payload = dict(login=new_courier['login'], password=new_courier['password'])
        payload[key] = empty_field
        with allure.step('Отправка запроса на авторизацию курьера с некорректными данными'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 400
                and response.json()['message'] == MessagesData.MESSAGE_LOG_IN_COURIER_WITHOUT_REQUIRED_FIELD)


    @allure.title('Невозможность авторизоваться курьером с некорректным значением поля')
    @pytest.mark.parametrize('key, wrong_field',
                             [
                                 ['login', CourierData.wrong_log_in_data['login']],
                                 ['password', CourierData.wrong_log_in_data['password']]
                             ],
                             ids=['wrong_login', 'wrong_password'])
    def test_log_in_courier_with_wrong_field_failure(self, key, wrong_field, new_courier):
        payload = dict(login=new_courier['login'], password=new_courier['password'])
        payload[key] = wrong_field
        with allure.step('Отправка запроса на авторизацию курьера с некорректными данными'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 404
                and response.json()['message'] == MessagesData.MESSAGE_LOG_IN_COURIER_WITH_WRONG_FIELD)