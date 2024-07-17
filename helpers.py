import requests
from faker import Faker
from urls import Urls
from endpoints import Endpoints
import allure


@allure.step('Генерация данных для регистрации курьера')
def generate_courier_correct_data():

    fake = Faker()
    courier_correct_data = {
        'login': fake.email(),
        'password': fake.password(),
        'firstName': fake.name()
    }
    return courier_correct_data


@allure.step('Регистрация нового курьера и возвращение данных для авторизации')
def register_new_courier_and_return_login_password():

    register_data = generate_courier_correct_data()
    login_data = {}
    url = f'{Urls.MAIN_URL}{Endpoints.CREATE_COURIER_EP}'
    response = requests.post(url, data=register_data)
    if response.status_code == 201:
        login_data = register_data
    return login_data


@allure.step('Генерация данных для регистрации курьера без обязательного поля')
def generate_courier_data_without_required_field(field):

    courier_incorrect_data = {}
    if field == 'login':
        courier_incorrect_data = generate_courier_correct_data()
        courier_incorrect_data['login'] = None
    elif field == 'password':
        courier_incorrect_data = generate_courier_correct_data()
        courier_incorrect_data['password'] = None
    return courier_incorrect_data


@allure.step('Генерация данных для регистрации курьера с уже используемым логином')
def generate_courier_data_with_exist_login():

    login_data_courier_1 = register_new_courier_and_return_login_password()
    register_data_courier_2 = generate_courier_correct_data()
    register_data_courier_2['login'] = login_data_courier_1['login']
    return register_data_courier_2


def get_courier_id(courier_data):

    url = f'{Urls.MAIN_URL}{Endpoints.LOGIN_COURIER_EP}'
    response = requests.post(url, data=courier_data)
    courier_id = response.json()['id']
    return courier_id


@allure.step('Удаление учетной записи курьера')
def delete_courier_data(courier_id):

    url = f'{Urls.MAIN_URL}{Endpoints.DELETE_COURIER_EP.format(id=courier_id)}'
    response = requests.delete(url)
    if response.status_code != 200:
        print('Problem: "Courier" test data was not deleted')