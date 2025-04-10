import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(full_transactions):
    generator = filter_by_currency(full_transactions, "USD")
    assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(generator) == {
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
    assert next(generator) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }


def test_filter_by_currency_no_such_currency(full_transactions):
    with pytest.raises(StopIteration):
        generator = filter_by_currency(full_transactions, "CHF")
        next(generator)


def test_filter_by_currency_empty_list():
    with pytest.raises(StopIteration):
        generator = filter_by_currency([], "USD")
        next(generator)


def test_transaction_description(full_transactions):
    descriptions = transaction_descriptions(full_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_description_empty_list():
    with pytest.raises(StopIteration):
        generator = transaction_descriptions([])
        next(generator)


@pytest.mark.parametrize("start, stop, expected", [
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (3, 5, ["0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),
    (300, 302, ["0000 0000 0000 0300", "0000 0000 0000 0301", "0000 0000 0000 0302"]),
    (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
])
def test_card_number_generator(start, stop, expected):
    generated = list(card_number_generator(start, stop))
    assert generated == expected
