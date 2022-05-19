#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# https://www.hackerrank.com/challenges/three-month-preparation-kit-pangrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

def pangrams(s):
    # Write your code here
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in s.lower():
        letters = letters.replace(i, '')

    return "pangram" if (len(letters) == 0) else "not pangram"


'''def main():
    # s = input("Enter a string: ")
    print(pangrams("We promptly judged antique ivory buckles for the next prize"))


main()'''
