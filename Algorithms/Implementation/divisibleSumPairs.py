#!/bin/python3

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
def divisibleSumPairs(n, k, ar):
    # Write your code here
    ar = sorted(ar)
    res = 0
    for i in range(len(ar)):
        for j in range(1, len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                res += 1
    return res
