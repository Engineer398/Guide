
"""
Bubble Sort
Пузырьковая сортировка
"""

def bubble_sort(array: list):
    """

    :param array: unsorted array
    :return: sorted array
    """
    lenght = len(array)

    for i in range(0, lenght - 1):
        reverse = False
        for j in range(0, lenght - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                reverse = True
        if reverse == False:
            return array
import random
import time

a = [random.randint(0, 100) for _ in range(100)]

print(bubble_sort(a))

