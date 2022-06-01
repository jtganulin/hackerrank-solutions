def timeConversion(s):
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

def main():
    s = input("Enter 12-hour format time string like hh:mm:ssPM: ")
    print(str(timeConversion(s)))


main()

