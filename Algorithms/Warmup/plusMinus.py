#!/bin/python3

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    # Write your code here
    res = {
        'pos': 0,
        'neg': 0,
        'zero': 0
    }
    for el in arr:
        if el > 0:
            res['pos'] += 1
        elif el == 0:
            res['zero'] += 1
        else:
            res['neg'] += 1

    print("{:.6f}\n{:.6f}\n{:.6f}".format(res['pos'] / len(arr), res['neg'] / len(arr), res['zero'] / len(arr)))
