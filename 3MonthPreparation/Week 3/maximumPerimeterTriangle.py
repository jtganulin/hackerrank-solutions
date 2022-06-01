#!/bin/python3

import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
#https://www.hackerrank.com/challenges/three-month-preparation-kit-maximum-perimeter-triangle/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks = sorted(sticks)
    temp = {}

    for i in range(len(sticks) - 2):
        # Use triangle inequality theorem to check for a triangle
        sub = [sticks[i], sticks[i + 1], sticks[i + 2]]
        a, b, c = sub
        if a + b > c and a + c > b and b + c > a:
            per = a + b + c
            if per in temp.keys():
                temp[per].append(sub)
            else:
                temp[per] = [sub]

    # No triangles were found
    if len(list(temp.keys())) == 0:
        return [-1]

    greatest = max(list(temp.keys()))
    # If there were more than one set of sides giving max perimeter
    if type(temp[greatest][0]) == list:
        res = temp[greatest][0]
        for sub in temp[greatest]:
            if max(sub) > max(res) or min(sub) > min(res):
                 res = sub

        return sorted(res)
    else:
        return sorted(temp[greatest])

    return [-1]

if __name__ == '__main__':
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    sys.stdout.write(' '.join(map(str, result)))

