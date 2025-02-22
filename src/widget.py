from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_in: str) -> str:
    """Функция делит полученные данные на 2 части и вторую часть маскирует"""
    first_part = ""
    second_part = ""
    for item in info_in:
        if item.isdigit():
            second_part += item
        else:
            first_part += item

    if len(second_part) == 16:
        second_part_masked = get_mask_card_number(int(second_part))
    else:
        second_part_masked = get_mask_account(int(second_part))

    return f"{first_part} {second_part_masked}"


def get_date(long_date: str) -> str:
    """Функция получает дату в длинном формате и возвращает в коротком"""
    date_obj = datetime.strptime(long_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(mask_account_card("3654108430135874305"))
    print(get_date())
