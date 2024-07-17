import pytest
import helpers
import allure


@pytest.fixture(scope='function')
def new_courier():
    new_courier = helpers.register_new_courier_and_return_login_password()
    yield new_courier
    courier_id = helpers.get_courier_id(new_courier)
    helpers.delete_courier_data(courier_id)