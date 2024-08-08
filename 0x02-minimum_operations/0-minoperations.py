#!/usr/bin/env python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file
"""


def minOperations(n):
    """
    will return minumum number of ops needed
    """
    num = 0
    i = 2
    if type(n) is not int or n <= 1:
        return 0
    while n != 1:
        if n % 1 == 0:
            n = n / i
            num = num + 1
        else:
            i = i + 1
    return num
