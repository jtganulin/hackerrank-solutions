def miniMaxSum(arr):
    # Write your code here
    res = sorted(arr)
    least = 0
    for i in res[0:4]:
        least += i

    greatest = 0
    for i in res[1:]:
        greatest += i

    print(str(least) + " " + str(greatest))
