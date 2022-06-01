#!/bin/python3

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#
#https://www.hackerrank.com/challenges/three-month-preparation-kit-two-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three

def twoArrays(k, A, B):
    # Write your code here
    # Sort A from least to greatest, B from greatest to least
    # In this way maximize probability that A[i] + B[i] >= k
    AP = sorted(A)
    BP = sorted(B, reverse=True)

    for i in range(len(AP)):
        if AP[i] + BP[i] < k:
            return "NO"

    return "YES"

