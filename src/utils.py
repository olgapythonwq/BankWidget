import json
import os

json_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'data', 'operations.json')
# print(json_path)


def get_operations(path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            operations = json.load(f)
            if isinstance(operations, list):     # Проверим, что данные являются списком
                return operations
            else:
                print("Ошибка: данные не являются списком.")
                return []
    except FileNotFoundError:
        print(f"Файл по пути {path} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return []


# if __name__ == '__main__':
#     print(get_operations(json_path))
