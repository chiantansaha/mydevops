#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    i=0 
    point_a=0
    point_b=0
    for i in range(len(a)):
        if a[i]==b[i]:
            pass
        elif a[i]>b[i]:
            point_a=point_a+1
        else:
            point_b=point_b+1
    return(point_a,point_b)

    

if __name__ == '__main__':
    fptr = open("ABCD.txt", 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
