import pytest
import requests
import helpers
import allure
from urls import Urls
from endpoints import Endpoints
from data import MessagesData


class TestCreateCourier:

    url = f'{Urls.MAIN_URL}{Endpoints.CREATE_COURIER_EP}'

    @allure.title('Успешная регистрация курьера')
    def test_create_courier_success(self):
        payload = helpers.generate_courier_correct_data()
        with allure.step('Отправка запроса на регистрацию курьера'):
            response = requests.post(self.url, data=payload)

        assert response.status_code == 201 and response.json()['ok'] == True


    @allure.title('Невозможность зарегестрироваться курьером с уже используемым логином')
    def test_create_courier_with_exist_login_failure(self, new_courier):
        payload = new_courier
        with allure.step('Отправка запроса на регистрацию курьера с некорректными данными'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 409 and
                response.json()['message'] == MessagesData.MESSAGE_CREATE_COURIER_WITH_EXIST_LOGIN)


    @allure.title('Невозможность зарегестрироваться курьером без обязательного поля')
    @pytest.mark.parametrize('incorrect_data',
                             [
                                 helpers.generate_courier_data_without_required_field('login'),
                                 helpers.generate_courier_data_without_required_field('password')
                             ],
                             ids=['create_without_login', 'without_password'])
    def test_create_courier_without_required_field_failure(self, incorrect_data):
        payload = incorrect_data
        with allure.step('Отправка запроса на регистрацию курьера с некорректными данными'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 400
                and response.json()['message'] == MessagesData.MESSAGE_CREATE_COURIER_WITHOUT_REQUIRED_FIELD)