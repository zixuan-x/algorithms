'''
two stack:
time: O(n) where n is the result string
space: O(n)
'''
class Solution:
    def decodeString(self, s: str) -> str:
        cur = ''
        number = 0
        numberStack = []
        stringStack = []
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c.isalpha():
                cur += c
            elif c == '[':
                numberStack.append(number)
                number = 0
                stringStack.append(cur)
                cur = ''
            else:  # c == ']'
                cur = stringStack.pop() + cur * numberStack.pop()    
        return cur

'''
one stack:
'''
class Solution:
    def decodeString(self, s: str) -> str:
        cur = ''
        number = 0
        stack = []
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c.isalpha():
                cur += c
            elif c == '[':
                stack.append(cur)
                stack.append(number)
                number = 0
                cur = ''
            else:  # c == ']'
                num = stack.pop()
                cur = stack.pop() + cur * num
        return cur