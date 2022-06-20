#!/bin/python3

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def diagonalDifference(arr):
    # Write your code here
    a = b = 0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][(len(arr) - 1) - i]

    return abs(a - b)
