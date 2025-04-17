from pprint import pformat
from unittest.mock import patch

import pytest

from main import main
from tests.conftest import full_transactions


# Создаём фикстуру, которая подменит функцию чтения из файла внутри main()
@pytest.fixture
def mock_file_processing(full_transactions):
    # Когда main() вызовет get_operations_from_xl(), вместо чтения настоящего XLSX, она получит full_transactions
    with patch('main.get_operations_from_xl', return_value=full_transactions),\
        patch('main.get_operations_from_csv', return_value=full_transactions),\
        patch('main.get_operations', return_value=full_transactions):  # json
        # print("[MOCK] get_operations_from_xl подменён, возвращаем:", full_transactions)
        yield


def test_main_from_json(mock_file_processing, full_transactions):
    user_inputs = ['1', 'EXECUTED', 'Нет', 'Нет', 'Да', 'карты']  # Пример пользовательских ответов для input()
    expected_output = [
        {
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
    ]
    with patch('builtins.input', side_effect=user_inputs), patch('main.pprint') as mock_pprint, \
         patch('builtins.print'):  # patch('builtins.print') - заглушаем обычный print, чтобы не засорять вывод во время теста
        main()
        printed = [pformat(val) for val in (call.args[0] for call in mock_pprint.call_args_list)]
        expected_str = pformat(expected_output)

        assert expected_str in printed


def test_main_from_csv(mock_file_processing, full_transactions):
    user_inputs = ['2', 'CANCELED', 'Нет', 'Да', 'Да', 'организации']
    expected_output = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    with patch('builtins.input', side_effect=user_inputs), patch('main.pprint') as mock_pprint, \
         patch('builtins.print'):
        main()
        printed = [pformat(val) for val in (call.args[0] for call in mock_pprint.call_args_list)]
        expected_str = pformat(expected_output)

        assert expected_str in printed


def test_main_from_excel(mock_file_processing, full_transactions):
    user_inputs = ['3', 'EXECUTED', 'Да', 'возрастанию', 'Нет', 'Да', 'организации']
    expected_output = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58Z",
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
    ]
    with patch('builtins.input', side_effect=user_inputs), patch('main.pprint') as mock_pprint, \
     patch('builtins.print'):
        main()
        printed = [pformat(val) for val in (call.args[0] for call in mock_pprint.call_args_list)]
        expected_str = pformat(expected_output)

        assert expected_str in printed
