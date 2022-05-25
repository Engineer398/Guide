"""
Модуль содержит примеры использования встроенных методов класса
"""
class InitDel:
    """
    __init__() - вызывается при создании экземпляра класса
    __del__() -  вызывается при удалении экземпляра класс
    """
    def __init__(self, *args, **kwargs):
        self.params = args
        self.kwparams = kwargs
    def __del__(self):
        print("Delete self of InitDel")

# example = InitDel(1,2,3, param1= 25, param_2= 32)
# del example

class Iter_Obj:
    """
    Create iter obj - numbers of Fibonachi
    __iter__() - call one time in before iteration
    __next__() - call each time were call __next__()
    """
    def __init__(self, start_1, start_2, num=10):
        """

        :param start_1: first number
        :param start_2: second number
        :param num: quantity of sequence fibonachi
        """
        self.start_1 = 0
        self.start_2 = 0
        self.first = start_1
        self.second = start_2
        self.num = num
        self.i = 0

    def __iter__(self):
        """
        reset counter
        :return: self   !!!!!!! dont forget it
        """
        self.i = 0  # reset counter
        self.start_1 = self.first # instalation start first value
        self.start_2 = self.second # instalation start second value
        return self # return self DONT FORGET IT

    def __next__(self):
        """

        :return: value or StopIteration()
        """
        self.i += 1
        if self.i > self.num:
            raise StopIteration() # Nessesary DONT FORGET IT
        else:
            self.start_1, self.start_2 = self.start_2, self.start_1 + self.start_2
        return self.start_2

# fib_9 = Iter_Obj(1, 1, 9)
#
# print(fib_9)
# for value in fib_9:
#     print(value)

class Context_manager:
    def __enter__(self):
        "calls were with XXXX as YYYY:   were YYYYY it's return value"
        return False # it's manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        "process exceptions and broadcat it in parameters, called when closed manager"
        print(f"exc_type: {exc_type}, exc_val: {exc_val}, exc_tb: {exc_tb}")

# with Context_manager() as manager:
#     print("Do something")
#     print(manager)

class Callable_obj:
    def __init__(self, n: int):
        self.n = n

    def __call__(self, x: int):
        return self.n * x

# obj = Callable_obj(n= 4)
# print(obj(x=3))
