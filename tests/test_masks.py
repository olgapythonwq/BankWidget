import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    with pytest.raises(TypeError):
        get_mask_card_number("abc")
    with pytest.raises(ValueError):
        get_mask_card_number(70007922896063)
    with pytest.raises(TypeError):
        get_mask_card_number()


@pytest.mark.parametrize("invalid_card_type", ["abc",
                                               True,
                                               [1, 2],
                                               {1: "One"}])
def test_get_mask_card_number_invalid_type(invalid_card_type):
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_card_type)


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"
    with pytest.raises(ValueError):
        get_mask_account(73654108430135874)
    with pytest.raises(TypeError):
        get_mask_account()
    with pytest.raises(ValueError):
        get_mask_account(73654108430135874874874)


@pytest.mark.parametrize("invalid_account_type", ["abc",
                                               True,
                                               [1, 2],
                                               {1: "One"}])
def test_get_mask_account_invalid_type(invalid_account_type):
    with pytest.raises(TypeError):
        get_mask_account(invalid_account_type)
