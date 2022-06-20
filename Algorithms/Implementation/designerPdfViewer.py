#!/bin/python3

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    # Write your code here
    maxHeight = 0
    for c in word:
        pos = h[ord(c) - ord('a')]
        if pos > maxHeight:
            maxHeight = pos

    return maxHeight * len(word)
