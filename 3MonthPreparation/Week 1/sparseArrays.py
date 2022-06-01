#!/bin/python3

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    results = [0 for i in range(len(queries))]
    for i in range(len(queries)):
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                results[i] += 1
    return results

