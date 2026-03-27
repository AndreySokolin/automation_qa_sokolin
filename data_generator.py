from faker import Faker
import random
import string


class DataGenerator:
    """Генератор тестовых данных"""

    def __init__(self):
        self.faker = Faker()

    @staticmethod
    def random_string(length: int = 10) -> str:
        """Генерация случайной строки"""
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def random_number(min: int = 1, max: int = 100) -> int:
        """Генерация случайного числа"""
        return random.randint(min, max)

    @staticmethod
    def random_email() -> str:
        """Генерация случайного email"""
        faker = Faker()
        return faker.email()

    @staticmethod
    def random_username() -> str:
        """Генерация случайного имени пользователя"""
        faker = Faker()
        return faker.user_name()

    @staticmethod
    def random_password(length: int = 12) -> str:
        """Генерация случайного пароля"""
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def test_user() -> dict:
        """Генерация данных тестового пользователя"""
        faker = Faker()
        return {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "phone": faker.phone_number(),
            "address": faker.address(),
            "city": faker.city(),
            "zip_code": faker.zipcode()
        }

    @staticmethod
    def credit_card() -> dict:
        """Генерация тестовых данных кредитной карты"""
        return {
            "number": "4111111111111111",  # Тестовая карта Visa
            "expiry": "12/25",
            "cvv": "123"
        }

    @staticmethod
    def product_data() -> dict:
        """Генерация данных тестового продукта"""
        faker = Faker()
        return {
            "name": faker.catch_phrase(),
            "description": faker.text(max_nb_chars=200),
            "price": round(random.uniform(10, 1000), 2),
            "sku": ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        }

    @staticmethod
    def get_test_items(count: int = 5) -> list:
        """Генерация списка тестовых элементов"""
        items = []
        for i in range(count):
            items.append({
                "id": i + 1,
                "name": DataGenerator.random_string(10),
                "value": DataGenerator.random_number(1, 1000)
            })
        return items