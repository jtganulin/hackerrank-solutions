#!/bin/python3


#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
# https://www.hackerrank.com/challenges/arrays-ds/problem

def reverseArray(a):
    # Write your code here
    for i in range(len(a) // 2):
        # Go just up to the middle of the array
        # swapping on either side of it
        temp = a[len(a) - i - 1]
        a[len(a) - i - 1] = a[i]
        a[i] = temp

    return a


if __name__ == "__main__":
    b = list(map(int, input("Enter an array to reverse like 1 2 3: ").rstrip().split()))
    reverseArray(b)
