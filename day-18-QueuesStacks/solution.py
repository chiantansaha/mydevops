from collections import deque


class Solution:
    def __init__(self):
        self.queue = deque()
        self.stack = list()
        print(self.queue)
        print(self.stack)

    def pushCharacter(self, character):
        self.stack.append(character)

    def enqueueCharacter(self, character):
        self.queue.append(character)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()


# read the string s
s = input().strip()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    print(s[i])
    obj.pushCharacter(s[i])
    #print(obj.pushCharacter(s[i]))
    obj.enqueueCharacter(s[i])
    #print(obj.enqueueCharacter(s[i]))

#pc = obj.pushCharacter(s)
#pe = obj.enqueueCharacter(s)
#print(pc)
#print(pe)

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
