"""
Пример реализации декораторов
"""
#
# Simple decorator
#

def decorator_simple_one(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@decorator_simple_one
def do_something_one():
    print("Do something one")

# do_something_one()

#
# Two decorators
#

def decorator_simple_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator_simple_two START")
        result = func(*args, **kwargs)
        print("Decorator_simple_two END")
        return result
    return wrapper

def decorator_simple_tree(func):
    def wrapper(*args, **kwargs):
        print("Decorator_simple_tree START")
        result = func(*args, **kwargs)
        print("Decorator_simple_tree END")
        return result
    return wrapper

@decorator_simple_two
@decorator_simple_tree
def do_something_two():
    print("Do something two")

# do_something_two() # = decorator_simple_two(decorator_simple_tree(do_something_two))

#
# Decorator class
#
# For each decorated functions created instanse of class
# For one decorated functions created one instanse of class

class Decorator():

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print("Decorator START")
        result = self.func(*args, **kwargs)
        print("Decorator END")
        print(self.count)
        return result



@Decorator
def do_something_tree(number: int):
    print("do_something_tree Number = {0}".format(number))
    return number

@Decorator
def do_something_four():
    print("do_something_four")

# a = do_something_tree(3)
# b = do_something_four()

#
# Decorator with args, kwargs
#

def decorator_with_args(*args_decorator, **kwargs_decorator):
    def outher(func):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args_decorator):
                print("{0}: {1}".format(i + 1, arg), end="\t", sep=" ")
            print()
            result = func(*args, **kwargs)
            for key, value in kwargs_decorator.items():
                print("Key:{0}, Value: {1}".format(key, value), sep=" ")
            return result
        return wrapper
    return outher

@decorator_with_args(2, 1, 3, end="End", start="Start")
def do_something_five(number: int):
    print("do_something_five Number = {0}".format(number))
    return number

# do_something_five(3)

#
# Class decorator with args
#

class Decorator_with_Args:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(self.args):
                print("{0}: {1}".format(i + 1, arg), end="\t", sep=" ")
            print()
            result = func(*args, **kwargs)
            for key, value in self.kwargs.items():
                print("Key:{0}, Value: {1}".format(key, value), sep=" ")
            return result
        return wrapper

@Decorator_with_Args(1, 2, 3, key="Tomorrow", display="YES")
def do_something_six(number: int):
    print("do_something_six Number = {0}".format(number))
    return number

# do_something_six(10)

#
# Documentation
#

from functools import wraps

def decorator_simple_with_doc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("START")
        result = func(*args, **kwargs)
        print("END")
        return result
    return wrapper

@decorator_simple_with_doc
def do_something_seven(number: int):
    """
    Function don't do anything, only print
    :param number: int
    :return: number
    """
    print("do_something_seven Number = {0}".format(number))
    return number

# print(do_something_seven.__doc__)

#
# Example - TIMER
#

import time
from datetime import datetime

def decorator_timer(func):
    def wrapper(*args, **kwargs):
        timer = datetime.now()
        result = func(*args, **kwargs)
        timer = (datetime.now() - timer).total_seconds() * 1000

        print("Время выполнения функции {0} равно {1} мс".format(func.__name__, timer))
        return result
    return wrapper

@decorator_timer
def sum_with_delay(a: int, b: int, delay: int):
    time.sleep(delay)
    print("a = {0} b = {1} delay = {2} резульат = {3}".format(a, b, delay, a + b))

# sum_with_delay(1, 1, 0)
# sum_with_delay(2, 2, 1)

#
# Singleton - Decorated class
# Singleton — это класс с одним экземпляром
# Его можно сохранить как атрибут функции-обертки и вернуть при запросе.
# Это полезно в тех случаях, когда, например, ведется работа с соединением с базой данных.

def singleton(cls):
    '''Класс Singleton (один экземпляр)'''
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass

print('старт')
first_one = TheOne()
second_one = TheOne()
print(id(first_one))
print(id(second_one))
print('конец')





