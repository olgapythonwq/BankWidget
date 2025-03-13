from typing import Any, Dict, Generator, Optional

list_of_transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]


def filter_by_currency(transactions: list[dict], currency: str = 'USD') -> Generator:
    """Функция, принимающая список транзакций и возвращающая генератор,
        который поочередно возвращает транзакции с указанной валютой"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Функция, принимающая список транзакций и возвращающая генератор,
        который поочередно возвращает описание каждой операции"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция, генерирующая номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, stop + 1):
        # Форматируем число как строку из 16 цифр
        card_number = f"{num:016d}"
        # Разбиваем на блоки по 4 цифры и возвращаем с пробелами
        yield " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])


usd_transactions = filter_by_currency(list_of_transactions, "USD")
for index in range(2):
    print(next(usd_transactions))


descriptions = transaction_descriptions(list_of_transactions)
for i in range(3):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Нет транзакций.")


for new_card_number in card_number_generator(1, 5):
    print(new_card_number)


for new_card_number in card_number_generator(6, 10):
    print(new_card_number)


chf_transactions = filter_by_currency(list_of_transactions, "CHF")
for index in range(1):
    try:
        print(next(chf_transactions))
    except StopIteration:
        print("Нет транзакций.")
