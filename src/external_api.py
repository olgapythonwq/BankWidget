import os

import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))  # Загрузка переменных из .env-файла
API_KEY = os.getenv('API_KEY')
# print(API_KEY)


url = "https://api.apilayer.com/exchangerates_data/convert"

headers = {"apikey": API_KEY}


def calculate_amount_of_transaction(transaction: dict) -> float | None:
    """Функция возвращает сумму транзакций в рублях с учетом курса валют"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        amount = transaction["operationAmount"]["amount"]
        currency_from = transaction["operationAmount"]["currency"]["code"]
        currency_to = "RUB"
        payload = {"amount": amount,
                   "from": currency_from,
                   "to": currency_to}
        response = requests.get(url, headers=headers, params=payload)
        status_code = response.status_code
        # print(status_code)
        if status_code != 200:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
        else:
            result_amount = response.json()["result"]
            return float(result_amount)


# if __name__ == '__main__':
#     print(calculate_amount_of_transaction(
#     {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
# }))
#
#     print(calculate_amount_of_transaction(
#     {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
# }))
