#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(k):
    sum_of_k=0
    k_numbers=[i for i in str(k)]
    for item in k_numbers:
        sum_of_k=sum_of_k+int(item)
    return(sum_of_k)        

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    for _ in range(n):
        result = superDigit(k)
        k = result

    print(result)
