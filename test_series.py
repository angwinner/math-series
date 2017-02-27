from __future__ import print_function
import pytest


def test_fibo_1():
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibo_2():
    from series import fibonacci
    assert fibonacci(2) == 1


def test_fibo_3():
    from series import fibonacci
    assert fibonacci(3) == 1


def test_fibo_25():
    from series import fibonacci
    assert fibonacci(25) == 46368


def test_fibo_iter_1():
    from series import fibonacci_iter
    assert fibonacci_iter(1) == 0


def test_fibo_iter_2():
    from series import fibonacci_iter
    assert fibonacci_iter(2) == 1


def test_fibo_iter_3():
    from series import fibonacci_iter
    assert fibonacci_iter(3) == 1


def test_fibo_iter_25():
    from series import fibonacci_iter
    assert fibonacci_iter(25) == 46368


def test_lucas_1():
    from series import lucas
    assert lucas(1) == 2


def test_lucas_2():
    from series import lucas
    assert lucas(2) == 1


def test_lucas_3():
    from series import lucas
    assert lucas(3) == 3


def test_lucas_25():
    from series import lucas
    assert lucas(25) == 103682

def test_sum_series_fib_1():
    from series import sum_series
    assert sum_series(1) == 0


def test_sum_series_luc_1():
    from series import sum_series
    assert sum_series(1, 2, 1) == 2


def test_sum_series_other_1():
    from series import sum_series
    assert sum_series(1, 5, 3) == 5


def test_sum_series_fib_2():
    from series import sum_series
    assert sum_series(2) == 1


def test_sum_series_luc_2():
    from series import sum_series
    assert sum_series(2, 2, 1) == 1


def test_sum_series_other_2():
    from series import sum_series
    assert sum_series(2, 5, 3) == 3


def test_sum_series_fib_3():
    from series import sum_series
    assert sum_series(3) == 1


def test_sum_series_luc_3():
    from series import sum_series
    assert sum_series(3, 2, 1) == 3


def test_sum_series_other_3():
    from series import sum_series
    assert sum_series(3, 5, 3) == 8


def test_sum_series_fib_25():
    from series import sum_series
    assert sum_series(25) == 46368


def test_sum_series_luc_25():
    from series import sum_series
    assert sum_series(25, 2, 1) == 103682


def test_sum_series_other_5():
    from series import sum_series
    assert sum_series(5, 5, 3) == 19
    