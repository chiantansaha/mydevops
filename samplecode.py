import os,sys
import numpy as np

a = np.array([1,2,3,4,5])
p = np.percentile(a, 50) #Returns 50th percentile, e.g. median
print(p)

'''

d = {}
a = type(d)
print(a)


a = 5//2

print(a)


f = None
 
for i in range (5):
    with open("data.txt", "w") as f:
        print("i = ",i)
        if i > 2:
            f.write("SS")
            break
 
f.closed



try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occured")
except "someError":
    print("someError has occured")

'''
