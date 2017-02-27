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
