from unittest.mock import mock_open, patch

import pandas as pd

from src.fin_transactions import (
    count_transactions_per_category,
    filter_transactions_by_description,
    get_category_list,
    get_operations_from_csv,
    get_operations_from_xl
)


def test_get_operations_from_csv():
    # Пример данных CSV в виде строки
    mock_csv_data = "id;amount;date\n1;100;2025-03-30\n2;200;2025-03-31\n"
    # Используем mock_open для того, чтобы замокать поведение open
    with patch('builtins.open', mock_open(read_data=mock_csv_data)):
        result = get_operations_from_csv('mocked_path.csv')
        expected_result = [ {'id': '1', 'amount': '100', 'date': '2025-03-30'},
                            {'id': '2', 'amount': '200', 'date': '2025-03-31'}]
        assert result == expected_result


def test_get_operations_from_xl():
    # Замокаем данные в виде pandas DataFrame
    mock_df = pd.DataFrame({'id': [1, 2],
                            'amount': [100, 200],
                            'date': ['2025-03-30', '2025-03-31']})
    # Используем patch для того, чтобы замокать pandas.read_excel
    with patch('pandas.read_excel', return_value=mock_df):
        result = get_operations_from_xl('mocked_path.xlsx')
        expected_result = [{'id': 1, 'amount': 100, 'date': '2025-03-30'},
                           {'id': 2, 'amount': 200, 'date': '2025-03-31'}]
        assert result == expected_result

def test_filter_transactions_by_description(full_transactions):
    assert filter_transactions_by_description(full_transactions, "Перевод со счета на счет") == [
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
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


def test_get_category_list(full_transactions):
    assert get_category_list(full_transactions) == ["перевод организации",
                                                    "перевод со счета на счет",
                                                    "перевод с карты на карту"]


def test_count_transactions_per_category(full_transactions):
    assert count_transactions_per_category(full_transactions, ["перевод организации", "перевод со счета на счет", "перевод с карты на карту"]) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1
    }
