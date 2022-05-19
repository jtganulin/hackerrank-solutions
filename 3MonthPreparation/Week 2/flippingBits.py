#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
# https://www.hackerrank.com/challenges/three-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

def flippingBits(n):
    # Write your code here
    # 0xFFFFFFFF is 0b11111111111111111111111111111111
    # XORing the 2 will flip the bits in 'n'
    return (n ^ 0xFFFFFFFF)

