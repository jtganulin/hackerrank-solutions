#!/bin/python3

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#
# https://www.hackerrank.com/challenges/angry-professor/problem
def angryProfessor(k, a):
    # Write your code here
    count = 0
    for i in a:
        if i < 1:
            count += 1

    return "YES" if count < k else "NO"
