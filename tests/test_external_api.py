import os
from unittest.mock import patch
from src.external_api import calculate_amount_of_transaction
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))  # Загрузка переменных из .env-файла
API_KEY = os.getenv('API_KEY')


@patch('requests.get')
def test_calculate_amount_of_transaction(mock_get):
    mock_get.return_value.json.return_value = {"result": 5000.0}  # Мокируем возврат json() с нужным значением 5000.0
    mock_get.return_value.status_code = 200  # Статус код успешного ответа

    # Пример транзакции для теста
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }

    # Вызываем функцию и проверяем результат
    result = calculate_amount_of_transaction(transaction)

    # Проверяем, что результат равен ожидаемому значению
    assert result == 5000.0

    # Проверяем, что запрос был сделан с правильными параметрами
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": API_KEY},
        params={"amount": '8221.37', "from": "USD", "to": "RUB"}
    )


def test_calculate_amount_of_transaction_RUB():
    assert calculate_amount_of_transaction({
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }) == 31957.58

