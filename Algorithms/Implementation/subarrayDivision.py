#!/bin/python3

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    # Write your code here
    count = 0

    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1

    return count
