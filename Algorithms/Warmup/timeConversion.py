#!/bin/python3

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    # Write your code here
    result = ""
    resultH = s[:2]
    resultM = s[3:5]
    resultS = s[6:8]
    AM = s[-2:]

    if resultH == "12":
        if AM == "AM":
            result = "00" + ":" + resultM + ":" + resultS
        else:
            result = "12" + ":" + resultM + ":" + resultS
    else:
        if AM == "AM":
            result = resultH + ":" + resultM + ":" + resultS
        else:
            result = "{:2d}".format(int(resultH) + 12) + ":" + resultM + ":" + resultS

    return result
