def get_mask_card_number(card_number: int) -> str:
    """Функция маскирующая номер карты"""
    if type(card_number) is not int:
        raise TypeError("Номер карты должен состоять только из цифр")
    else:
        card_number_string = str(card_number)
        if len(card_number_string) != 16:
            raise ValueError("В номере карты должно быть 16 цифр")
    return f"{card_number_string[:4]} {card_number_string[4:6]}** **** {card_number_string[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскирующая номер счёта"""
    if type(account_number) is not int:
        raise TypeError("Номер счёта должен состоять только из цифр")
    else:
        if len(str(account_number)) != 20:
            raise ValueError("В номере счёта должно быть 20 цифр")
        else:
            account_number_string = str(account_number)
    return f"**{account_number_string[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
