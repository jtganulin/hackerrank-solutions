#!/bin/python3

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# https://www.hackerrank.com/challenges/migratory-birds/problem
def migratoryBirds(arr):
    # Write your code here
    freq = [0] * len(arr)
    for el in arr:
        freq[el] += 1

    posMax = []
    maxEl = max(freq)
    for i in range(len(freq)):
        if freq[i] == maxEl:
            posMax.append(i)

    return min(posMax)
