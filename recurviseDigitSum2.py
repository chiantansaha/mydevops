#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n,k):
    number_to_deal_with = ""
    p=0
    while p<k:
        number_to_deal_with=number_to_deal_with+str(n)
        p=p+1
    print(number_to_deal_with)
    sum_of_k = sumOfNumbers(number_to_deal_with)
    return(sum_of_k)
    
def sumOfNumbers(nu):
    sum_of_n=0
     
    n_numbers=[i for i in str(nu)]
    for item in n_numbers:
        sum_of_n=sum_of_n+int(item)
        #sumOfNumbers(sum_of_n)
    while sum_of_n > 9 :
        sum_of_n=sumOfNumbers(sum_of_n)
    return(sum_of_n)        

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    result = superDigit(n,k)

    print(result)
