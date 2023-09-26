#!/usr/bin/python3
"""
pascals triangle
"""


def get_pascal(num, arr):
    """
    recurse
    """
    if (num == 0):
        return arr
    if (len(arr[-1]) == 1):
        arr.append([1, 1])
        return get_pascal(num - 1, arr)
    newarr = []
    first = 0
    second = 1
    newarr.append(arr[-1][0])
    while (second < len(arr[-1])):
        newarr.append(arr[-1][first] + arr[-1][second])
        first += 1
        second += 1
    newarr.append(arr[-1][-1])
    arr.append(newarr)
    return get_pascal(num - 1, arr)


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s
    triangle of n
    """
    if n <= 0 or type(n) is not int:
        return [[]]
    n -= 1
    return get_pascal(n, [[1]])
