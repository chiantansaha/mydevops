#!/bin/python3

import math
import os
import random
import re
import sys

def nRotation(a,d):
    i=0
    while i < d:
        pp=a[0]
        a.append(pp)
        del a[0]
        i=i+1
    return(a)

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    postRotation = nRotation(a,d)
    for item in postRotation:
        print(item,end=" ")
