#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# https://www.hackerrank.com/challenges/three-month-preparation-kit-lonely-integer?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
def lonelyinteger(a):
    # Write your code here
    results = {}
    for i in range(len(a)):
        if str(a[i]) not in results.keys():
            results[str(a[i])] = 0
        results[str(a[i])] += 1

    for k, v in results.items():
        if v == 1:
            return k


def main():
    arr = [1, 1, 2, 2, 3, 3, 4]
    print(lonelyinteger(arr))


main()
