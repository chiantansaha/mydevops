def first_last6(nums):
  if nums[0]==6 or nums[-1]==6:
    return True
  else:
    return False

def main():
    s=first_last6([6, 1, 2, 3])
    print(s)