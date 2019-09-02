#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr,n):

    negArr=[]
    zeroArr=[]
    posArr=[]

    for item in arr:
        if item == 0:
            zeroArr.append(item)
        elif item < 0:
            negArr.append(item)
        else:
            posArr.append(item)
    
    posProp=len(posArr)/n
    negProp=len(negArr)/n
    zerProp=len(zeroArr)/n

    return([posProp,negProp,zerProp])
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    nowArray = plusMinus(arr,n)
    for item in nowArray:
        print(item)
