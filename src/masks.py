def get_mask_card_number(card_number: int) -> str:
    """Функция маскирующая номер карты"""
    card_number_string = str(card_number)
    return f"{card_number_string[:4]} {card_number_string[4:6]}** **** {card_number_string[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскирующая номер счёта"""
    account_number_string = str(account_number)
    return f"**{account_number_string[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
