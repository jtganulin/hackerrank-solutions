#!/bin/python3

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    # Write your code here
    return candles.count(max(candles))
