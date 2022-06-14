import string

# Функция capwords () переводит в верхний регистр первую букву каждого слова в строке.
def string_capword(s: str):
    print(s)
    print(string.capwords(s))

# Пример
# s = "The quick brown fox jumped over the lazy dog."
# string_capword(s)

# str.join()
def str_join(iter_obj:iter, split:str):
    print(split.join(iter_obj))

# str_join(["banana", "apple", "house"], "\n")

# string.template()
def string_template():
    values = {"var": "foo"}
    t = string.Template("""
    Variable        : $var
    Escape          : $$
    Variable in text: ${var}iable
    """)
    print(t.substitute(values))

#string_template()

# str.format()
def str_format():
    template = "Name: {name}, age: {age}"
    kwargs = {"name" : "John", "age" : 21}
    result = template.format(**kwargs)
    print(result)

# str_format()

# string.Template faster then str.format()

import time

def timer(func:()):
    def wapper(*args, **kwargs):
        timer = time.time()
        result = func(*args, **kwargs)
        timer = time.time() - timer
        print(f"Time: {timer}")
        return result
    return wapper

def cycle(num):
    def inner(func):
        def wrapper(*args, **kwargs):

            for _ in range(num):
                func(*args, **kwargs)

        return wrapper
    return inner


@timer
@cycle(100000)
def calc_format():
    template = "Name: {name}, age: {age}"
    result = template.format(name="John", age=25)


@timer
@cycle(1000)
def calc_template():
    template = string.Template("Name: ${name}, age: ${age}")
    result =  template.substitute(name="John", age=25)

# calc_format()
# calc_template()










