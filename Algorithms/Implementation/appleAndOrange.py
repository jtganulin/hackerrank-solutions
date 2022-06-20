#!/bin/python3

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#
# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    resApples = 0
    resOranges = 0

    for el in apples:
        if el + a >= s and el + a <= t:
            resApples += 1

    for el in oranges:
        if el + b >= s and el + b <= t:
            resOranges += 1

    print(str(resApples) + "\n" + str(resOranges))
