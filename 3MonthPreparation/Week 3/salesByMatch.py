#!/bin/python3

import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
#https://www.hackerrank.com/challenges/three-month-preparation-kit-sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three

def sockMerchant(n, ar):
    # Write your code here
    freq = [0] * 100
    count = 0

    if n <= 1:
        return 0

    for i in range(len(ar)):
        # print(str(i) + " " + str(ar[i]))
        freq[ar[i] - 1] += 1

    for el in freq:
        count += el // 2

    return count



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    sys.stdout.write(str(result) + '\n')
    # fptr.write(str(result) + '\n')
    # fptr.close()
