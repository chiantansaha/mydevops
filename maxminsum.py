#!/bin/python3

import math
import os
import random
import re
import sys
import itertools 

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    lst = [] 
    for i in itertools.permutations(arr,4): 
        # provides all permutations of the list values, 
        # store them in list to find max 
        lst.append(i)
    print(lst)
    maxsum= sum(max(lst))
    minsum= sum(min(lst))
    #return(maxsum,minsum)
    print(minsum,maxsum)
# This code is contributed by Raman Monga 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
