import requests


def test_different_response_codes():
    """Демонстрация работы с разными HTTP статусами"""

    # Используем httpbin для тестирования разных ответов
    base = "https://httpbin.org"

    # Тест 1: Успешный запрос
    print(" Тест 1: Успешный GET запрос")
    response = requests.get(f"{base}/get")
    print(f"   Статус: {response.status_code}")
    assert response.status_code == 200

    # Тест 2: Создание ресурса
    print(" Тест 2: POST запрос с данными")
    data = {"name": "Тестовые данные"}
    response = requests.post(f"{base}/post", json=data)
    print(f"   Статус: {response.status_code}")
    print(f"   Отправленные данные получены: {response.json()['json'] == data}")
    assert response.status_code == 200

    # Тест 3: Запрос к несуществующему ресурсу (404)
    print(" Тест 3: Обработка ошибки 404")
    response = requests.get(f"{base}/status/404")
    print(f"   Статус: {response.status_code} - Ресурс не найден")
    assert response.status_code == 404

    # Тест 4: Задержка ответа (таймаут)
    print(" Тест 4: Работа с таймаутами")
    try:
        # Просим сервер ответить через 3 секунды, но ждем только 2
        requests.get(f"{base}/delay/3", timeout=2)
    except requests.exceptions.Timeout:
        print(" Таймаут сработал корректно")