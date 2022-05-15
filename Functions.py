
#=======================================================================================================================
def show_zip():
    """
    Class zip()

    zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.

       >>> list(zip('abcdefg', range(3), range(4)))
       [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

    The zip object yields n-length tuples, where n is the number of iterables
    passed as positional arguments to zip().  The i-th element in every tuple
    comes from the i-th iterable argument to zip().  This continues until the
    shortest argument is exhausted.

    If strict is true and one of the arguments is exhausted before the others,
    raise a ValueError.
    :return:
    """

    array_1 = [1, 2, 3]
    array_2 = [6, 7, 8]
    array_3 = [11, 12, 13]
    obj_zip = zip(array_1, array_2, array_3)
    for x, y, z in obj_zip:
        print(x, y, z)

#show_zip()

# 1 6 11
# 2 7 12
# 3 8 13

#=======================================================================================================================
def show_map():
    """
        map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    :return:
    """

    digits = ["1", " 2", "3"]
    print(list(map(int, digits)))

    num_1 = [1, 2, 3]
    num_2 = [4, 5, 6]
    print(list(map(lambda x, y: x + y, num_1, num_2)))

# show_map()

# [1, 2, 3]
# [5, 7, 9]

#=======================================================================================================================
def show_filter():
    """
        filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    :return:
    """
    test = [1, 2, "ab", 4, "b", 5, "c"]
    print(
        list(
            filter(
                lambda x: isinstance(x, str), test
            )
        )
    )

# show_filter()

# ['ab', 'b', 'c']

#=======================================================================================================================






