#!/bin/python3

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#
# https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k, height):
    # Write your code here
    return max(height) - k if max(height) - k > 0 else 0
