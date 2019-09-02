import sys
class Solution:
    def checkReverse(self,myword):
        return myword[::-1]
    

# read the string s
s = input().strip()
# Create the Solution class object
obj = Solution()

revObj = obj.checkReverse(s)
if s == revObj :
    print("Its a panildrome")
    

