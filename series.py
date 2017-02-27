from __future__ import print_function


def fibonacci(n):
    """ return the nth element of the Fibonacci sequence """
    if n == 1:
        return 0

    if n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_iter(n):
    """ return the nth element of the Fibonacci sequence """
    if n == 1:
        return 0

    if n == 2:
        return 1

    i = 0
    j = 1
    k = 0
    """ element k of the Fibonacci sequence is the sum of the two
    previous elements i and j """
    for s in range(n-2):
        k = i + j
        i = j
        j = k
    return k


def lucas(n):
    """ returns the nth element of the Lucas sequence """
    if n == 1:
        return 2

    if n == 2:
        return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n, first=0, second=1):
    """ return the nth element of a series where each element is the
    sum of the two previous elements """

    if n == 1:
        return first

    if n == 2:
        return second

    return sum_series(n-1, first, second) + sum_series(n-2, first, second)
