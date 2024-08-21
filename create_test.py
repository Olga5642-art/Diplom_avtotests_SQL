# Ольга Марченко, 20-я когорта — Финальный проект. Инженер по тестированию плюс

# Импорт необходимых модулей и данных для запроса
import sender_stand_request
import data

#Тест на успешное получение заказа по треку
def test_get_zakaz_by_track ():
        # Вызов функции post_new_zakaz для создания нового заказа
        response_zakaz = sender_stand_request.post_new_zakaz(data.zakaz_body)
        # Получение трекере созданного заказа
        track = response_zakaz.json()['track']
        # В переменную response сохраняется результат запроса на получение заказа по треку
        response = sender_stand_request.get_zakaz_by_track(track)
        # Проверяется, что код ответа равен 200
        assert response.status_code == 200

