#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    myresult = n * k % 9 or 9
    return(myresult)
           

if __name__ == '__main__':
    fptr = open("myrecursive.txt", 'w')

    #nk = input().split()

    #n = int(nk[0])

    #k = int(nk[1])

    n, k = map(int, input().split())
    print( )

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
