# Working solution


def staircase(num_stairs):
    n = num_stairs - 1
    #print(n)
    for stairs in range(0, num_stairs):
        print(' ' * n, '#' * stairs)
        #break
        n -= 1
    print('#' * num_stairs)
staircase(6)




'''    
def staircase(n):
    for i in range(0, n): # n rows 
        print(' '*(n-i-1) + '#'*(i+1)) # first print n-i-1 spaces followed by i '#'

staircase(6)

'''


'''
def staircase(num_stairs):
    n = num_stairs - 1
    for stairs in range(num_stairs):
        print(" " * n, '#' * stairs)
        n -= 1
    print('#' * num_stairs)
staircase(6)
'''
'''
def staircase(n):

    #print(n)
    for stairs in range(0, n):
        print(n,stairs)
        #break
        n -= 1

staircase(6)

'''
