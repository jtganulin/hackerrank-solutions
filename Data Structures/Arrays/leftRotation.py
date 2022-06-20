#!/bin/python3

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
# https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        arr.append(arr.pop(0))

    return arr

    # O(nm)
    # for i in range(d):
    #     first = arr[0]
    #     for j in range(0, len(arr) - 1):
    #         arr[j] = arr[j + 1];
    #
    #     arr[len(arr) - 1] = first
    # return arr
