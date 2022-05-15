"""
Алгоритмы сортировки
"""
import random
import time
import functools

def decorator_timer(func: ()):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timer = time.time()
        result = func(*args, **kwargs)
        timer = time.time() - timer
        print("Time = {0} ms".format(timer))
        return result
    return wrapper


"""
Bubble Sort
Пузырьковая сортировка
"""
@decorator_timer
def bubble_sort(array: list):
    """

    :param array: unsorted array
    :return: sorted array
    """
    lenght = len(array)

    for i in range(0, lenght):
        reverse = False
        for j in range(0, lenght - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                reverse = True
        if reverse == False:
            return array

# a = [random.randint(0, 100) for _ in range(100)]
# print(bubble_sort(a))

"""
Сортировка перемешиванием
Shaker (cocktail, ripple, shuffle, shuttle) sort
"""
@decorator_timer
def shake_sort(array: list):
    """

    :param array: unsorted array
    :return: sort array
    """
    lenght_list = array.__len__()
    for n in range(0, lenght_list):
        reverse = False
        for i in range(n, lenght_list - 1 - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                reverse = True
        for j in range(lenght_list - 1, n, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                reverse = True

        if reverse == False:
            return array

    return array
#
# test_array = [random.randint(1, 100) for x in range(100)]
# print(shake_sort(test_array))

"""
Сортировка расчёской
Comb sort
"""
@decorator_timer
def comb_sort(array: list):
    lenght = array.__len__()
    step = int(lenght / 1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < lenght:
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                swap = 1
            i += 1
        if step > 1:
            step = int(step / 1.247)
    return array
#
# test_array = [random.randint(1, 100) for x in range(100)]
# print(comb_sort(test_array))



