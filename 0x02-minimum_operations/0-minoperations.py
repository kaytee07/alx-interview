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
    if n == 1:
        return 0
    
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + dp[i // j] + 1)

    return dp[n] if dp[n] != float('inf') else 0
