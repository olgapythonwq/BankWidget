import logging
import os

from config import LOGS_DIR

masks_logger = logging.getLogger('masks_log')
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, 'masks.log'), 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскирующая номер карты"""
    if type(card_number) is not int:
        masks_logger.error('Номер карты должен состоять только из цифр')
        raise TypeError("Номер карты должен состоять только из цифр")
    else:
        card_number_string = str(card_number)
        if len(card_number_string) != 16:
            masks_logger.error('В номере карты должно быть 16 цифр')
            raise ValueError("В номере карты должно быть 16 цифр")
    masks_logger.info('Номер карты замаскирован')
    return f"{card_number_string[:4]} {card_number_string[4:6]}** **** {card_number_string[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскирующая номер счёта"""
    if type(account_number) is not int:
        masks_logger.error('Номер счёта должен состоять только из цифр')
        raise TypeError("Номер счёта должен состоять только из цифр")
    else:
        if len(str(account_number)) != 20:
            masks_logger.error('В номере счёта должно быть 20 цифр')
            raise ValueError("В номере счёта должно быть 20 цифр")
        else:
            masks_logger.info('Номер счёта замаскирован')
            account_number_string = str(account_number)
    return f"**{account_number_string[-4:]}"


# if __name__ == "__main__":
#     print(get_mask_card_number(7000792289606361))
#     print(get_mask_account(73654108430135874305))
