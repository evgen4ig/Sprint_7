class MessagesData:

    MESSAGE_CREATE_COURIER_WITH_EXIST_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
    MESSAGE_CREATE_COURIER_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для создания учетной записи'
    MESSAGE_LOG_IN_COURIER_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для входа'
    MESSAGE_LOG_IN_COURIER_WITH_WRONG_FIELD = 'Учетная запись не найдена'


class CourierData:

    empty_log_in_data = {
        'login': '',
        'password': ''
    }

    wrong_log_in_data = {
        'login': 'wrong@login',
        'password': 'Wrong_pass123!'
    }


class OrderData:

    order_data = {
        'firstName': 'Test',
        'lastName': 'Testov',
        'address': 'Moscow, Pushkina, 17',
        'metroStation': 7,
        'phone': '+7(905)193 17 71',
        'rentTime': 3,
        'deliveryDate': '2024-05-05',
        'comment': 'test_comment 123!',
        'color': []
    }

    order_list_data = {
        'courierId': None,
        'nearestStation': '["1"]',
        'limit': 10,
        'page': 1
    }