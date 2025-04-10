from os import remove

import pytest

from src.decorators import log, my_function


def test_log():
    assert log


def test_log_ok(capsys) -> None:    # Тест на правильный вывод
    my_function(2, 2)
    captured = capsys.readouterr()
    assert "ok" in captured.out


def test_log_ko(capsys) -> None:    # Тест на неправильный вывод
    my_function(2, "2")
    captured = capsys.readouterr()
    assert "Inputs" in captured.out


def test_log_file():
    @log("temp.txt")
    def summator(*args):
        return sum(args)
    result = summator(1, 2, 3, 4)
    with open("temp.txt", "r") as file:
        line_in_file = file.read()
        assert result == 10
        assert "ok" in line_in_file
    remove("temp.txt")
