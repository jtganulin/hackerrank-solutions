def divisibleSumPairs(n, k, ar):
    # Write your code here
    ar = sorted(ar)
    res = 0
    for i in range(len(ar)):
        for j in range(1, len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                res += 1
    return res

