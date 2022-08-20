import bisect
import random

"""
Модуль bisect реализует алгоритм вставки элементов в список, обеспечивающий
поддержание сортированного состояния списка.
"""

def insort():
    array = [random.randint(1, 100) for _ in range(20)]
    l = []

    for i in array:
        bisect.insort(l, i)

        if len(str(i)) > 10:
            print(f"new: {i}, array: {l}")
        else:
            print(f"new: {i},  array: {l}")

# insort()


