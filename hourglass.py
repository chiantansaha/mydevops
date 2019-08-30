#!/bin/python3

import math
import os
import random
import re
import sys

def _get_hourglass_sum(arr, i, j):
    sum = 0
    sum += arr[i-1][j-1]
    sum += arr[i-1][j]
    sum += arr[i-1][j+1]
    sum += arr[i][j]
    sum += arr[i+1][j-1]
    sum += arr[i+1][j]
    sum += arr[i+1][j+1]
    return sum

# Complete the hourglassSum function below.
def hourglassSum(arr):

    # start max_hourglass_sum at smallest possible hourglass
    max_hourglass_sum = 0
    for i in range(1,5):
        for j in range(1, 5):
            current_hourglass_sum = _get_hourglass_sum(arr, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    return(max_hourglass_sum)

if __name__ == '__main__':
    fptr = open("HOURGLASS.txt", 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
