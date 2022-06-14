import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invelid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 2


# IntEnum  ведет себя еще как и число (арифметические операции)
class BugStatusInt(enum.IntEnum):

    new = 7
    incomplete = 6
    invelid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 2

def show_enum():
    for status in BugStatus:
        print(f"Name: {status.name}, Value: {status.value}")

# show_enum()

def func_enum():
    ErrorStatus = enum.Enum(names="new incomplete wont_fix in_progress", value="ErrorStatus")
    for error in ErrorStatus:
        print(f"{error.name}: {error.value}")

# func_enum()

def func_enum_2():
    ErrorStatus = enum.Enum(value="ErrorStatus", names=[("new", 7), ("old", 5)])
    for status in ErrorStatus:
        print(f"{status.name}: {status.value}")

# func_enum_2()

class aaa(enum.Enum):
    a = enum.auto()
    b = enum.auto()

def show_auto():
    for element in aaa:
        print(f"{element.name}: {element.value}")

# show_auto()












