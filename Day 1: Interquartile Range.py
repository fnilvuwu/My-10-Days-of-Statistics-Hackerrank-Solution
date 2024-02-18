#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    myList = []
    for e, f in zip(values, freqs):
        myList.append([e] * f)
    myList = [element for sublist in myList for element in sublist]
    myList.sort()
    t=int(len(myList)/2)
    if len(myList)%2==0:
        L=myList[:t]
        U=myList[t:]
    else:
        L=myList[:t]
        U=myList[t+1:]
    result = round(median(U) - median(L), 1)
    print("{:.1f}".format(result))
    

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
