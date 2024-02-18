#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median
#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    arr.sort()
    t=int(len(arr)/2)
    if len(arr)%2==0:
        L=arr[:t]
        U=arr[t:]
    else:
        L=arr[:t]
        U=arr[t+1:]

    return int(median(L)), int(median(arr)), int(median(U))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
