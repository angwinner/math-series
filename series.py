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

def in_parens(text):
    text_list = text.split('(')
    text_end = text_list[1]
    text_in = text_end.split(')')
    return text_in[0]

def main():
    print("This module defines functions that implement mathematical series")
    print("where each element is the sum of the two previous elements.")
    print("fibonacci(n):")
    print("    Returns the nth value in the Fibonacci sequence")
    print("lucas(n):")
    print("    Returns the nth value in the Lucas sequence")
    print("sum_series(n, [first], [second]):")
    print("    Returns the nth value in series with the first and second")
    print("    elements specified, or defaults to 0, 1 (Fibonacci)")
    resp = input("Would you like to try it? (y/n): ")
    if resp.lower() == 'n':
        return

    while True:
        cmd = input(">>>")
        if cmd.lower().startswith('q'):
            return
        if cmd.lower() == 'exit':
            return

        if cmd.startswith('fibonacci'):
            n = int(in_parens(cmd))
            print(fibonacci(n))
        elif cmd.startswith('lucas'):
            n = int(in_parens(cmd))
            print(lucas(n))
        elif cmd.startswith('sum_series'):
            args = in_parens(cmd)
            arg_list = args.split(',')
            n = int(arg_list[0].strip())
            if len(arg_list) == 3:
                first = int(arg_list[1].strip())
                second = int(arg_list[2].strip())
                print(sum_series(n, first, second))
            else:
                print(sum_series(n))

        else:
            print("Sorry, I didn't understand that.")
            print("fibonacci(n), lucas(n), sum_series(n, [first], [second]), or quit")


if __name__ == '__main__':
    main()

