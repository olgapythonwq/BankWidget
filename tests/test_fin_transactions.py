from unittest.mock import mock_open, patch

import pandas as pd

from src.fin_transactions import get_operations_from_csv, get_operations_from_xl


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
