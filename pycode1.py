def first_last6(nums):
  if nums[0]==6 or nums[-1]==6:
    return True
  else:
    return False

def common_end(a, b):
  if (a[-1] == b[-1] or a[0] == b[0]):
    return True
  else:
    return False

def sum3(nums):
  return(sum(nums))

def reverse3(nums):
  new_nums=nums.reverse()
  return(new_nums)

def main():
    #s=first_last6([6, 1, 2, 3])
    #print(s)
    s=reverse3([6, 1, 2, 3])
    print(s)
    