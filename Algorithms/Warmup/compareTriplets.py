#!/bin/python3

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

def compareTriplets(a, b):
    # Write your code here
    res = [0, 0]
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] > b[i]:
                res[0] += 1
            else:
                res[1] += 1
    return res
