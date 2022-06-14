import array
import time
import tempfile
import binascii
# сищный array
# но со ссылокчным данными, нет привязки к адресу

# wrap_timer for tst

def decorator_timer(func):
    def wrapper(*args, **kwargs):
        timer = time.time()
        result = func(*args, **kwargs)
        timer = time.time() - timer
        print(f"func: {func.__name__} time: {timer}")
        return result
    return wrapper


def init_array():
    tst_array = array.array("L", [1, 2, 3, 10]) # if tst_array < 0 and "L" -> Error
    print(f"tst_array = {tst_array}")
    tst_array[0], tst_array[1], tst_array[2] = 3, 2, 1
    print(f"tst_array = {tst_array}")
    print(f"Slice = {tst_array[0:2]}")
    tst_array.extend([1, 2, 3])
    tst_array.append(20)
    print(f"Count of two = {tst_array.count(2)}")


# init_array()
N = 1000000
@decorator_timer
def check_time_array():
    tst_array = array.array("q", range(N))
    for i in range(N):
        tst_array[i] = i

@decorator_timer
def check_time_list():
    tst_list = [i for i in range(N)]
    for i in range(N):
        tst_list[i] = i

# list INT faster then array INT
# check_time_array()
# check_time_list()

def to_bytes():
    a = array.array("i", range(5))
    print(f"A1: {a}")
    as_bytes = a.tobytes()
    print(f"A1_bytes: {binascii.hexlify((as_bytes))}")

    a2 = array.array("i")
    a2.frombytes(as_bytes)
    print(f"A2: {a2}")

# to_bytes()

def show_swap():

    def to_hex(a:array.array):
        chars_per_item = a.itemsize * 2
        hex_version = binascii.hexlify(a)
        num_chunks = len(hex_version)
        for i in range(num_chunks):
            start = i * chars_per_item
            end = start + chars_per_item
            yield hex_version[start:end]

    start = int("0x12345678", 16)
    end = start + 5
    a1 = array.array("i", range(start, end))
    a2 = array.array("i", range(start, end))
    a2.byteswap()
    fmt = "{:>12} {:>12} {:>12} {:>12}"
    print(fmt.format('-' * 12, '-' * 12, "-" * 12, ' - ' * 12))
    fmt = '{!r:>12} {:12} {!r:>12} {:12}'
    for values in zip(to_hex(a1), a1, to_hex(a2), a2):
        print(fmt.format(*values))


# show_swap()

