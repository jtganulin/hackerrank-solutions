#!/bin/python3

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def breakingRecords(scores):
    # Write your code here
    minScore = maxScore = scores[0]
    minTimes = maxTimes = 0
    for i in range(1, len(scores)):
        if scores[i] < minScore:
            minScore = scores[i]
            minTimes += 1
        elif scores[i] > maxScore:
            maxScore = scores[i]
            maxTimes += 1

    return [maxTimes, minTimes]
