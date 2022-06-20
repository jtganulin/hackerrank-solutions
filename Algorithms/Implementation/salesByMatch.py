#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
# https://www.hackerrank.com/challenges/sock-merchant/problem
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
