# Импорт необходимых модулей и данных для запроса
import configuration
import requests
import data

# Определение функции для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Определение функции для отправки GET-запроса на получение заказа по треку
def get_order_by_track (track):
    # Выполнение GET-запроса с использованием URL из конфигурационного файла и параметра t
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params={"t":track})

