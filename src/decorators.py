from functools import wraps
from time import perf_counter
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[..., Any]:
    """Декоратор, логирующий начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""
    def inner(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            try:
                result = func(*args, **kwargs)
                stop = perf_counter()
                result_time = stop - start
                if filename:
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(f"{func.__name__} ok in {result_time:.6f} seconds\n")
                else:
                    print(f"{func.__name__} ok in {result_time:.5f} seconds")
            except Exception as e:
                stop = perf_counter()
                result_time = stop - start
                if filename:
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs} in {result_time:.5f} seconds\n")
                else:
                    print(f"{func.__name__}  error: {e}. Inputs: {args}, {kwargs} in {result_time:.5f} seconds")
            else:
                return result
        return wrapper
    return inner


# @log(filename="mylog.txt")
# def my_function(x: int, y: int) -> int:
#     """Функция суммирует два числа и возвращает результат"""
#     return x + y


@log('')
def my_function(x: int, y: int) -> int:
    """Функция суммирует два числа и возвращает результат"""
    return x + y


if __name__ == '__main__':
    print(my_function(1, "2"))

    # print(my_function(1, "2"))
