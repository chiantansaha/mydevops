def count_evens(nums):
    n=i=0
    for item in nums:
        if item%2==1:
            pass
        else:
            n=n+1
    return n

def main():
    m = count_evens([2, 1, 2, 3, 4])
    print(m)

main()