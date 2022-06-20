#!/bin/python3

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        a = arr.pop(0)
        arr.append(a)

    return arr

# def rotateLeft(d, arr):
#     # Write your code here
#     if len(arr) == 1:
#         return arr
#
#     while d > 0:
#         for i in range(len(arr) - 1):
#             j = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#         d -= 1
#     return arr

if __name__ == "__main__":
    d = int(input("Enter the amount of shifts: "))
    go = list(map(int, input("Enter the array values like 1 2 3...: ").rstrip().split()))
    print("\nAfter " + str(d) + " shifts, the array is: \n")
    print(' '.join(map(str, rotateLeft(d, go))))
