#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
  mysum = 0
  mycount = 0
  for i in range(n) :
    if s[i]=='U':
        mysum = mysum+1
        if mysum==0:
            mycount=mycount+1

    else:
        mysum=mysum-1
  return(mycount)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
