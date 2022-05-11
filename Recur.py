"""
Модуль содержит примеры рекурсий
"""

def factorial(num : int):
    """
    Факториал числа
    :param num: число
    :return: факториал числа
    """
    if num == 1:
        return 1
    return num * factorial(num - 1)


def sum_array(array: list, size: int):
    """
    Сумма массива
    :param array: list
    :param size: размер lista
    :return: сумма lista
    """
    if size == 0:
        return 0
    return array[size - 1] + sum_array(array, size - 1)


def pow_num(num: int, degree: int):
    """
    Возведение числа в степень
    :param num: число
    :param degree: степень
    :return: результат
    """
    if degree == 0:
        return 1
    return num * pow_num(num, degree - 1)

def is_polyndrom(string: str):
    if len(string) % 2 != 0:
        return False
    elif len(string) == 0:
        return True
    else:
        if





