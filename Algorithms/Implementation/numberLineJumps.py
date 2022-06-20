#!/bin/python3

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    for i in range(10001):
        if (x1 + v1 * i) == (x2 + v2 * i):
            return "YES"
    return "NO"
