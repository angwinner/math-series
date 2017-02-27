from __future__ import print_function


def fibonacci(n):
    """ returns the nth element of the Fibonacci sequence """
    if n == 1:
        return 0

    if n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_iter(n):
    """ returns the nth element of the Fibonacci sequence """
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
