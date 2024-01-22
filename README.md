Sprint_7

class TestCreatingCourier
    test_can_create_courier - Успешное создание курьера
    test_cannot_create_two_identical_couriers - Невозможно создать двух одинаковых курьеров
    test_not_login_required_field - Попытка создать курьера без указания login
    test_not_password_required_field - Попытка создать курьера без указания password

class TestLoginCourier
    test_true_courier_authorization - Успешная авторизация курьера
    test_courier_authorization_not_login - Создание курьера без указания login
    test_courier_authorization_not_password - Создание курьера без указания password
    test_courier_authorization_wrong - Создание курьера с указанием неверных данных

class TestGettingListOrders
    test_getting_list_orders - Получение списка заказов по id курьера
    test_getting_10_free_orders_from_list_orders - Получение списка 10 доступных заказов для курьера
    test_gettind_list_order_couriers_by_metro - Получение списка заказов по указанию станции метро

class TestCreatingAnOrder
    test_true_creating_an_order - Успешное создание заказа
