from pprint import pprint

from src.fin_transactions import (
    filter_transactions_by_description,
    get_category_list,
    get_operations_from_csv,
    get_operations_from_xl,
    path_to_csv,
    path_to_xl
)
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operations, json_path

greeting = "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
menu = 'Выберите необходимый пункт меню:\n' \
       '1. Получить информацию о транзакциях из JSON-файла\n'\
       '2. Получить информацию о транзакциях из CSV-файла\n'\
       '3. Получить информацию о транзакциях из XLSX-файла'
filters = ('Введите статус, по которому необходимо выполнить фильтрацию.\n'
           'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
sort_date = 'Отсортировать операции по дате? Да/Нет'
ascending = 'Отсортировать по возрастанию или по убыванию?'
what_currency = 'Выводить только рублевые транзакции? Да/Нет'
word_filter = 'Отфильтровать список транзакций по определенному слову в описании? Да/Нет'
category_list = get_category_list(get_operations_from_xl(path_to_xl))


def main():
    """Функция взаимодействующая с пользователем"""
    print(f'{greeting}\n{menu}')

    while True:
        user_choice = input()
        try:
            if int(user_choice) == 1:
                print(f'Для обработки выбран JSON-файл.\n{filters}')
                transactions = get_operations(json_path)
                break
            elif int(user_choice) == 2:
                print(f'Для обработки выбран CSV-файл.\n{filters}')
                transactions = get_operations_from_csv(path_to_csv)
                break
            elif int(user_choice) == 3:
                print(f'Для обработки выбран XLSX-файл.\n{filters}')
                transactions = get_operations_from_xl(path_to_xl)
                break
            else:
                print(f'Пункта "{user_choice}" в меню нет. {menu}')
        except ValueError:
            print(f'Пункта "{user_choice}" в меню нет. {menu}')

    while True:
        user_choice_2 = input()
        if user_choice_2.lower() == 'EXECUTED'.lower():
            print(f'Операции отфильтрованы по статусу "EXECUTED".\n{sort_date}')
            filtered_transactions = filter_by_state(transactions, 'EXECUTED')
            break
        elif user_choice_2.lower() == 'CANCELED'.lower():
            print(f'Операции отфильтрованы по статусу "CANCELED".\n{sort_date}')
            filtered_transactions = filter_by_state(transactions, user_choice_2.upper())
            break
        elif user_choice_2.lower() == 'PENDING'.lower():
            print(f'Операции отфильтрованы по статусу "PENDING".\n{sort_date}')
            filtered_transactions = filter_by_state(transactions, user_choice_2.upper())
            break
        else:
            print(f'Статус операции "{user_choice_2}" недоступен. {filters}')

    while True:
        user_choice_3 = input()
        if user_choice_3.lower() == 'Да'.lower():
            print(f'Операции будут отсортированы по дате.\n{ascending}')
            while True:
                user_choice_4 = input()
                if user_choice_4.lower() in ['по возрастанию', 'возрастанию']:
                    print(f'Операции будут отсортированы по дате по возрастанию.\n{what_currency}')
                    sorted_filtered_transactions = sort_by_date(filtered_transactions, reverse=False)
                    break
                elif user_choice_4.lower() in ['по убыванию', 'убыванию']:
                    print(f'Операции будут отсортированы по дате по убыванию.\n{what_currency}')
                    sorted_filtered_transactions = sort_by_date(filtered_transactions, reverse=True)
                    break
                else:
                    print(f'Ваш ответ "{user_choice_4}" непонятен. {ascending}')
            break
        elif user_choice_3.lower() == 'Нет'.lower():
            print(f'Операции не будут отсортированы по дате.\n{what_currency}')
            break
        else:
            print(f'Ваш ответ "{user_choice_3}" непонятен. {sort_date}')

    while True:
        user_choice_5 = input()
        if user_choice_5.lower() == 'Да'.lower():
            print(f'Будут выведены только рублевые транзакции.\n{word_filter}')
            if user_choice_3.lower() == 'Нет'.lower():
                rub_filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
            else:
                rub_sorted_filtered_transactions = list(filter_by_currency(sorted_filtered_transactions, "RUB"))
            break
        elif user_choice_5.lower() == 'Нет'.lower():
            print(f'Будут выведены все транзакции.\n{word_filter}')
            if user_choice_3.lower() == 'Нет'.lower():
                all_currencies_filtered_transactions = filtered_transactions
            else:
                all_currencies_sorted_filtered_transactions = sorted_filtered_transactions
            break
        else:
            print(f'Ваш ответ "{user_choice_5}" непонятен. {what_currency}')

    while True:
        user_choice_6 = input()
        if user_choice_6.lower() == 'Нет'.lower():
            print('Распечатываю итоговый список транзакций.')
            if user_choice_5.lower() == 'Да'.lower() and user_choice_3.lower() == 'Нет'.lower():
                result = rub_filtered_transactions
            elif user_choice_5.lower() == 'Да'.lower() and user_choice_3.lower() == 'Да'.lower():
                result = rub_sorted_filtered_transactions
            elif user_choice_5.lower() == 'Нет'.lower() and user_choice_3.lower() == 'Нет'.lower():
                result = all_currencies_filtered_transactions
            else:
                result = all_currencies_sorted_filtered_transactions
            break
        elif user_choice_6.lower() == 'Да'.lower():
            print('Укажите, что должно быть в описании.')
            while True:
                user_choice_7 = input()
                matches = [phrase for phrase in category_list if user_choice_7.lower() in phrase.lower()]
                if matches:
                    print('Распечатываю итоговый список транзакций.')
                    if user_choice_5.lower() == 'Да'.lower() and user_choice_3.lower() == 'Нет'.lower():
                        result = filter_transactions_by_description(rub_filtered_transactions, user_choice_7)
                    elif user_choice_5.lower() == 'Да'.lower() and user_choice_3.lower() == 'Да'.lower():
                        result = filter_transactions_by_description(rub_sorted_filtered_transactions, user_choice_7)
                    elif user_choice_5.lower() == 'Нет'.lower() and user_choice_3.lower() == 'Нет'.lower():
                        result = filter_transactions_by_description(all_currencies_filtered_transactions,
                                                                    user_choice_7)
                    else:
                        result = filter_transactions_by_description(all_currencies_sorted_filtered_transactions,
                                                                    user_choice_7)
                    break
                else:
                    print(f'Ваш ответ "{user_choice_7}" не подходит. Выберите из: {category_list}')
            break
        else:
            print(f'Ваш ответ "{user_choice_6}" непонятен. {word_filter}')
    pprint(result)
    result_count = len(result)
    print(f"Всего банковских операций в выборке: {result_count}")


if __name__ == '__main__':
    main()
