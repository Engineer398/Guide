"""
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
"""
def task():
    sign = 0

    def oper(n_1, n_2):
        if sign == 0:
            return n_1 + n_2
        elif sign == 1:
            return n_1 - n_2
        elif sign == 2:
            return n_1 * n_2
        elif sign == 3:
            return n_1 / n_2
        else:
            return 0


    def digit(num, n):
        if n == None:
            return num
        else:
            return oper(num, n)


    def zero(n=None):  # your code here
        return digit(0, n)


    def one(n=None):  # your code here
        return digit(1, n)


    def two(n=None):  # your code here
        return digit(2, n)


    def three(n=None):  # your code here
        return digit(3, n)


    def four(n=None):  # your code here
        return digit(4, n)


    def five(n=None):  # your code here
        return digit(5, n)


    def six(n=None):  # your code here
        return digit(6, n)


    def seven(n=None):  # your code here
        return digit(7, n)


    def eight(n=None):  # your code here
        return digit(8, n)


    def nine(n=None):  # your code here
        return digit(9, n)

    def plus(n):  # your code here
        nonlocal sign
        sign = 0
        return n

    def minus(n):  # your code here
        nonlocal sign
        sign = 1
        return n

    def times(n):  # your code here
        nonlocal sign
        sign = 2
        return n

    def divided_by(n):  # your code here
        nonlocal sign
        sign = 3
        return n

    print(seven(times(five())))
    print(four(plus(nine())))
    print(eight(minus(three()))) # must return 5
    print(six(divided_by(two()))) # must return 3

task()