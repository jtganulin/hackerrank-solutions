#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# https://www.hackerrank.com/challenges/three-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

def diagonalDifference(arr):
    # Write your code here
    primary = secondary = 0
    for i in range(len(arr)):
        # Primary
        primary += arr[i][i]
        # Secondary
        secondary += arr[i][len(arr[i]) - 1 - i]

    return abs(primary - secondary)

