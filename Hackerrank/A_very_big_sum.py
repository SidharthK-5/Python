"""
Question: Complete the 'aVeryBigSum' function below.

The function is expected to return a LONG_INTEGER.
The function accepts LONG_INTEGER_ARRAY ar as parameter.
"""

import os


def aVeryBigSum(ar):
    # Write your code here
    r = sum(ar)
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
