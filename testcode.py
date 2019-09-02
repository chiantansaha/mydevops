n, k = map(int, input().split())
print( n * k % 9 or 9)


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    sum_of_k=0
    k_numbers=[i for i in str(k)]
    for item in k_numbers:
        sum_of_k=sum_of_k+int(item)
    superDigit(n-1, sum_of_k)
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
