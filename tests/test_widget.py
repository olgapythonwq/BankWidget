import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum  7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет  **4305"


@pytest.mark.parametrize("info_in, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum  7000 79** **** 6361"),
    ("Master Card 7000792289606362", "Master Card  7000 79** **** 6362"),
    ("Visa Infinity 7000792289606363", "Visa Infinity  7000 79** **** 6363"),
    ("Счет 73654108430135874305", "Счет  **4305"),
    ("Счет 73654108430135874303", "Счет  **4303")
])
def test_mask_account_card_variables(info_in, expected):
    assert mask_account_card(info_in) == expected


def test_mask_account_card_wrong_card_number():
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum 70007922896063")


def test_mask_account_card_no_card_number():
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum ")


def test_mask_account_card_wrong_account_number():
    with pytest.raises(ValueError):
        mask_account_card("Счет 7365410843013587430538")


def test_mask_account_card_no_account_number():
    with pytest.raises(ValueError):
        mask_account_card("Счет ")


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("date_in, expected", [
    ("2024-08-11T02:26:18.671407", "11.08.2024"),
    ("2023-03-12T02:26:18.671407", "12.03.2023"),
    ("2024-10-10T02:26:18.671407", "10.10.2024")
])
def test_get_date_variables(date_in, expected):
    assert get_date(date_in) == expected


@pytest.mark.parametrize("date_in, expected", [
    ("2024-08-11T02:26:18", ValueError),
    ("2023-03-12T", ValueError),
    ("2024-10-10", ValueError)
])
def test_get_date_wrong_format(date_in, expected):
    with pytest.raises(ValueError):
        get_date(date_in)


def test_get_date_empty():
    with pytest.raises(TypeError):
        get_date()
