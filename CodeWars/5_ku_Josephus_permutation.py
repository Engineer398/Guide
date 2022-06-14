"""
https://www.codewars.com/kata/555624b601231dc7a400017a/train/python
In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.

Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:

test.assert_equals(josephus_survivor(7,3),4)
test.assert_equals(josephus_survivor(11,19),10)
test.assert_equals(josephus_survivor(1,300),1)
test.assert_equals(josephus_survivor(14,2),13)
test.assert_equals(josephus_survivor(100,1),100)
"""

def josephus_survivor(n: int,k: int):
    """
    Josephus permutation
    :param n: number of people
    :param k: step
    :return: survival
    """

    circle = list(range(1, n + 1))
    index, last = -1, 0
    for i in range(n):
        index += k
        if index >= len(circle):
            index %= len(circle)
        last = circle.pop(index)
        index -= 1

    return last

print(josephus_survivor(7, 3))

