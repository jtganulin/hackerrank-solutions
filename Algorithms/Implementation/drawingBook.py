#!/bin/python3

# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#
# https://www.hackerrank.com/challenges/drawing-book/problem
def pageCount(n, p):
    # Write your code here
    return min([p//2, n//2 - p//2])
