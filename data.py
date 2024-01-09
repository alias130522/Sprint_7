import helpers


data_order = {
                "firstName": helpers.random_name(),
                "lastName": helpers.last_name(),
                "address": "Konoha, 142 apt.",
                "metroStation": int(helpers.random_metro_station()),
                "phone": helpers.generating_telefon_namber(),
                "rentTime": int(helpers.generating_rent_time()),
                "deliveryDate": helpers.generating_data_day(),
                "comment": "Saske, come back to Konoha",
                "color": ["BLACK"]
            }

url_scooter = 'http://qa-scooter.praktikum-services.ru/'
url_creating_courier = url_scooter + 'api/v1/courier'
url_creating_an_order = url_scooter + 'api/v1/orders'
url_courier_authorization = url_scooter + 'api/v1/courier/login'
url_getting_list_orders_courierId = url_scooter + 'api/v1/orders?courierId='
url_getting_10_free_orders = url_scooter + 'api/v1/orders?limit=10&page=0'
gettind_list_order_couriers_by_metro = '&nearestStation=["' + helpers.random_metro_station() + '"]'

fix_list_data = helpers.random_list()