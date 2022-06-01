def plusMinus(arr):
    # Write your code here
    # Positive, negative, zero
    res = [0, 0, 0]
    for i in range(len(arr)):
        if arr[i] == 0:
            res[2] += 1
        elif arr[i] < 0:
            res[1] += 1
        elif arr[i] > 0:
            res[0] += 1

    # Find proportion of positives
    pos = abs(float(res[0] / len(arr)))
    print("%.6f" % pos)

    neg = abs(float(res[1] / len(arr)))
    print("%.6f" % neg)

    zero = abs(float(res[2] / len(arr)))
    print("%.6f" % zero)

