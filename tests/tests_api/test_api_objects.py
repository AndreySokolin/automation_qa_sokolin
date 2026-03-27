# сайт https://restful-api.dev

from tests.tests_api.endpoint.create_object import CreateObject
from tests.tests_api.endpoint.update_object import UpdateObject
from tests.tests_api.endpoint.delete_object import DeleteObject
from tests.tests_api.endpoint.get_object import GetObject

payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }


def test_add_new_object():  # Создание объекта
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_response_name(payload["name"])



def test_get_new_object(obj_id):  # Чтение объекта
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(obj_id)
    get_object_endpoint.check_response_is_200()
    get_object_endpoint.check_response_id(obj_id)



def test_update_object(obj_id):  # Изменение объекта
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_by_id(obj_id, payload)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_response_name(payload["name"])
    update_object_endpoint.check_response_year(payload["data"]["year"])
    update_object_endpoint.check_response_price(payload["data"]["price"])
    update_object_endpoint.check_response_cpu_model(payload["data"]["CPU model"])


def test_delete_object(obj_id):  # Удаление объекта
    delete_object_endpoint = DeleteObject()
    get_object_endpoint = GetObject()

    delete_object_endpoint.delete_by_id(obj_id) # Удаляем
    delete_object_endpoint.check_response_is_200() # Проверили 200

    get_object_endpoint.get_by_id(obj_id) # Запросили повторно созданный объект
    get_object_endpoint.check_response_is_404()  # Проверили 404(не нашли)
