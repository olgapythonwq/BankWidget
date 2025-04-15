import csv
import os
import re
from collections import Counter

import pandas as pd

from config import ROOT_DIR

path_to_csv = os.path.join(ROOT_DIR, 'data', 'transactions.csv')
path_to_xl = os.path.join(ROOT_DIR, 'data', 'transactions_excel.xlsx')
path_to_json = os.path.join(ROOT_DIR, 'data', 'operations.json')


def get_operations_from_csv(path: str) -> list[dict]:
    """Функция принимает путь до CSV файла и возвращает транзакции в виде списка словарей"""
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)


def get_operations_from_xl(path: str) -> list[dict]:
    """Функция принимает путь до Excel файла и возвращает транзакции в виде списка словарей"""
    df = pd.read_excel(path_to_xl)
    return df.to_dict(orient='records')  # преобразует данные из объекта DataFrame или Series в словарь


def filter_transactions_by_description(transactions: list[dict], description) -> list[dict]:
    """Функция, принимающая банковские операции и строку поиска, возвращающая те, у которых
    в описании есть данная строка"""
    pattern = re.compile(re.escape(description), re.IGNORECASE)  # .escape() - Экранирование спецсимволов
    result = []
    for transaction in transactions:
        if not isinstance(transaction.get('description'), str):  # Если описание в транзакции отсутствует
            continue
        else:
            if pattern.search(transaction.get('description')):
                result.append(transaction)
    return result


def get_category_list(transactions: list[dict]) -> list[str]:
    """Функция, принимающая банковские операции и возвращающая список категорий из description"""
    category_list = []
    for transaction in transactions:
        if not isinstance(transaction.get('description'), str):  # Если описание в транзакции отсутствует
            continue
        else:
            if transaction.get('description').lower() not in category_list:
                category_list.append(transaction.get('description').lower())
    return category_list


def count_transactions_per_category(transactions: list[dict], category_list: list[str]) -> dict:
    """Функция, принимающая банковские операции и список категорий операций, возвращающая словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""
    list_of_descriptions = []
    for transaction in transactions:
        if not isinstance(transaction.get('description'), str):  # Если описание в транзакции отсутствует
            continue
        else:
            if transaction.get('description').lower() in category_list:
                list_of_descriptions.append(transaction.get('description'))
    counted = Counter(list_of_descriptions)
    return counted


# if __name__ == '__main__':
    # get_operations_from_csv(path_to_csv)
    # print(get_operations_from_csv(path_to_csv)[:5])
    # get_operations_from_csv(path_to_csv)
    # pprint(get_operations_from_xl(path_to_xl))
    # pprint(filter_transactions_by_description(get_operations_from_xl(path_to_xl), 'счета'))
    # print(get_category_list(get_operations_from_xl(path_to_xl)))
    # print(count_transactions_per_category(get_operations_from_xl(path_to_xl),
# get_category_list(get_operations_from_xl(path_to_xl))))
    # pprint(get_operations_from_xl(path_to_xl))
