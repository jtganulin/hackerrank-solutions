#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# https://www.hackerrank.com/challenges/three-month-preparation-kit-mars-exploration/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
def marsExploration(s):
    # Write your code here
    errors = 0
    for i in range(0, len(s), 3):
        # print(str(i) + ": " + s[i] + "\t" + str(i + 1) + ": " + s[i + 1] + "\t" + str(i + 2) + ": " + s[i + 2])
        if s[i] != 'S':
            errors += 1
        if s[i + 1] != 'O':
            errors += 1
        if s[i + 2] != 'S':
            errors += 1

    return errors


'''def main():
    s = "SOSSPSSQSSOR"
    print(s)
    r = marsExploration(s)
    print(r)


main()
'''
