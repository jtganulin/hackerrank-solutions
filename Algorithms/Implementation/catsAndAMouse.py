#!/bin/python3

# Complete the catAndMouse function below.
# https://www.hackerrank.com/challenges/cats-and-a-mouse
def catAndMouse(x, y, z):
    if abs(z - y) == abs(z - x):
        return 'Mouse C'
    elif abs(z - y) > abs(z - x):
        return 'Cat A'
    else:
        return 'Cat B'
