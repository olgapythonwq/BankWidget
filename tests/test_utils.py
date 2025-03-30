from unittest.mock import mock_open, patch

from src.utils import get_operations, json_path


def test_get_operations():
    mock_data = '[{"1": "a"}, {"2": "b"}]'  # Мокируем содержимое JSON-файла
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:   # Используем patch для замены open на mock_open
        result = get_operations(json_path)

        expected_result = [{"1": "a"}, {"2": "b"}]  # Ожидаем, что результат будет списком с двумя элементами

        assert result == expected_result
        # Проверяем, что open был вызван один раз с нужными аргументами
        mock_file.assert_called_once_with(json_path, 'r', encoding='utf-8')


def test_get_operations_file_not_found():
    # Используем patch для замены open на mock_open, но файл не существует
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_operations(json_path)

        # Ожидаем, что функция вернет пустой список в случае ошибки
        assert result == []


def test_get_operations_json_decode_error():
    # Мокируем содержимое JSON-файла, передаем некорректный JSON
    mock_data = '{"1": "a", "2": "b"'  # Некорректный JSON, пропущена закрывающая фигурная скобка

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_operations(json_path)

        # Ожидаем, что функция вернет пустой список в случае ошибки JSON
        assert result == []


def test_get_operations_not_list():
    # Мокируем содержимое JSON-файла, словарём вместо списка
    mock_data = '{"1": "a", "2": "b"}'

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_operations(json_path)

        # Ожидаем, что функция вернет пустой список, потому что данные не являются списком
        assert result == []
