import unittest
import requests


class TestDelivery(unittest.TestCase):
    def setUp(self):
        # Здесь можно инициализировать какие-то переменные или выполнить другие действия перед каждым тестом
        self.base_url = "http://localhost:8080"  # Укажите адрес вашего сервера

    def test_create_delivery(self):
        # Отправляем POST-запрос на /delivery/{order_id}
        order_id = 123
        url = f"{self.base_url}/delivery/{order_id}"
        response = requests.post(url)

        # Проверяем, что сервер возвращает код статуса 200
        self.assertEqual(response.status_code, 200)

    def test_read_delivery(self):
        # Отправляем GET-запрос на /delivery/{order_id}
        order_id = 123
        url = f"{self.base_url}/delivery/{order_id}"
        response = requests.get(url)

        # Проверяем, что сервер возвращает код статуса 200
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()