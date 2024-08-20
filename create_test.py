# Ольга Марченко, 20-я когорта — Финальный проект. Инженер по тестированию плюс

# Импорт необходимых модулей и данных для запроса
import sender_stand_request
import data

#Тест на успешное получение заказа по треку
def test_poluchit_zakaz_po_track ():
        # В переменную response сохраняется результат запроса на получение заказа по треку
        response = sender_stand_request.get_zakaz_po_track()
        # Проверяется, что код ответа равен 200
        assert response.status_code == 200

