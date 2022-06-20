#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    # Write your code here
    results = []
    for el in grades:
        if el < 38:
            results.append(el)
            continue
        # Find the nearest multiple of 5
        mult = el % 5
        if (5 - mult) < 3:
            results.append((5 - mult) + el)
        else:
            results.append(el)

    return results
