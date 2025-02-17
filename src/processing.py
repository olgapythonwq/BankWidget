from datetime import datetime


def filter_by_state(list_of_dicts: list[dict], key: str = "EXECUTED") -> list[dict]:
    """Функция фильтрующая транзакции по статусу"""
    selected_list_of_dicts = []
    for dictionary in list_of_dicts:
        if dictionary["state"] == key:
            selected_list_of_dicts.append(dictionary)
    return selected_list_of_dicts


def sort_by_date(list_of_dicts: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирующая транзакции по дате"""
    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    for dictionary in list_of_dicts:
        if "date" not in dictionary or dictionary["date"] == "":
            raise ValueError("Дата отсутствует")
        try:
            datetime.strptime(dictionary["date"], date_format)
        except ValueError:
            raise ValueError("Неверный формат даты")
    sorted_list_of_dicts = sorted(list_of_dicts,
                                  key=lambda x: datetime.strptime(x["date"], date_format),
                                  reverse=reverse)
    return sorted_list_of_dicts


if __name__ == "__main__":
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                          "EXECUTED"))

    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                          "CANCELED"))

    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                       reverse=True))

    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                       reverse=False))
