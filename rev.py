#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    a.reverse()
    return a

def main():

    arr=[3,5,5,6]
    res = reverseArray(arr)
    #print(reverseArray(arr))
    print(res)
main()
