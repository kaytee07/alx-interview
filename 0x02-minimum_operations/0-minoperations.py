#!/usr/bin/python3
"""
min number of operations to print the H character n times
"""


def minoperations(n):
    """
    get the number of operations to print the H character

    Args:
        n is the number of times to print the H character

    Return:
        the minimum number of operations
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count
