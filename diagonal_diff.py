#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    i = 0
    j = 0
    dg1 = []
    dg2 = []
    while i < n and j < n:
        dg1.append(arr[i][j])
        i=i+1
        j=j+1
    print(dg1)
    ii=0
    jj=n-1
    while ii < n and jj >= 0:
        #print(arr[i][j])
        dg2.append(arr[ii][jj])
        ii=ii+1
        jj=jj-1
    print(dg2)

    summing_dg1=sum(dg1)
    summing_dg2=sum(dg2)

    differ = summing_dg2 - summing_dg1
    return(abs(differ))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
