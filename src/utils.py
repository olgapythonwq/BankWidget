import json
import logging
import os

from config import LOGS_DIR

json_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'data', 'operations.json')
# print(json_path)


utils_logger = logging.getLogger('utils_log')
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, 'utils.log'), 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def get_operations(path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        utils_logger.info('Файл operations.json открывается на чтение')
        with open(path, 'r', encoding='utf-8') as f:
            operations = json.load(f)
            if isinstance(operations, list):     # Проверим, что данные являются списком
                return operations
            else:
                utils_logger.error('Ошибка: данные не являются списком.')
                print("Ошибка: данные не являются списком.")
                return []
    except FileNotFoundError:
        utils_logger.error('Ошибка: файл по пути {path} не найден.')
        print(f"Файл по пути {path} не найден.")
        return []
    except json.JSONDecodeError as e:
        utils_logger.error(f'Ошибка декодирования JSON: {e}.')
        print(f"Ошибка декодирования JSON: {e}")
        return []
    except Exception as e:
        utils_logger.error(f"Неизвестная ошибка: {e}")
        print(f"Неизвестная ошибка: {e}")
        return []


if __name__ == '__main__':
    print(get_operations(json_path))
