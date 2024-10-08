#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file
"""


def minOperations(n):
    """
    returns the minimum no of operations needed
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    num = 0
    i = 2
    while n > 1:
        while n % i == 0:
            num += i
            n //= i
        i += 1
    return num
