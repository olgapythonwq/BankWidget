import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transactions, key="EXECUTED"):
    assert (filter_by_state(transactions, key="EXECUTED") ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
    assert (filter_by_state(transactions, key="CANCELED") ==
            [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])


def test_filter_by_state_wrong_state(transactions, key="POSTPONED"):
    assert filter_by_state(transactions, key="POSTPONED") == []


def test_filter_by_state_no_state(transactions, key=""):
    assert filter_by_state(transactions, key="POSTPONED") == []


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ("CANCELED", [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
    ("POSTPONED", []),
    ("", [])
])
def test_filter_by_state_various(transactions: list, state: str, expected: list):
    assert filter_by_state(transactions, key=state) == expected


@pytest.mark.parametrize("reverse, expected", [
    (True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29Z'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33Z'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25Z'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58Z'}]),
    (False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58Z'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25Z'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33Z'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29Z'}])
])
def test_sort_by_date(transactions, reverse, expected):
    assert sort_by_date(transactions, reverse) == expected


@pytest.mark.parametrize("reverse, expected", [
    (True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29Z'},
            {'id': 41428830, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29Z'},
            {'id': 41428831, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29Z'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33Z'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25Z'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58Z'},
            {'id': 939719571, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58Z'}]),
    (False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58Z'},
            {'id': 939719571, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58Z'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25Z'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33Z'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29Z'},
            {'id': 41428830, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29Z'},
            {'id': 41428831, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29Z'}])
])
def test_sort_by_date_same_date(same_date_transactions, reverse, expected):
    assert sort_by_date(same_date_transactions, reverse) == expected


def test_sort_by_date_wrong_date():
    with pytest.raises(ValueError):
        sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 41428830, 'state': 'EXECUTED', 'date': '2019-07'}])


def test_sort_by_date_no_date():
    with pytest.raises(ValueError):
        sort_by_date([{'id': 41428831, 'state': 'CANCELED', 'date': ''},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
