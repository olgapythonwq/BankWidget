import csv
import os

import pandas as pd

from config import ROOT_DIR

path_to_csv = os.path.join(ROOT_DIR, 'data', 'transactions.csv')
path_to_xl = os.path.join(ROOT_DIR, 'data', 'transactions_excel.xlsx')


def get_operations_from_csv(path: str) -> list[dict]:
    """Функция принимает путь до CSV файла и возвращает транзакции в виде списка словарей"""
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)


def get_operations_from_xl(path: str) -> list[dict]:
    """Функция принимает путь до Excel файла и возвращает транзакции в виде списка словарей"""
    df = pd.read_excel(path_to_xl)
    return df.to_dict(orient='records')  # преобразует данные из объекта DataFrame или Series в словарь


# if __name__ == '__main__':
    # get_operations_from_csv(path_to_csv)
    # print(get_operations_from_csv(path_to_csv)[:5])
    # get_operations_from_csv(path_to_csv)
    # print(get_operations_from_xl(path_to_xl))
