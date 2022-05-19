#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
# https://www.hackerrank.com/challenges/three-month-preparation-kit-counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
def countingValleys(steps, path):
    # Write your code here
    pos = valleys = 0
    for i in range(steps):
        if path[i] == "U":
            pos += 1
        else:
            pos -= 1
        if pos == 0 and path[i] == "U":
            valleys += 1

    return valleys

