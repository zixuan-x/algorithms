'''
recursion:
'''
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        self.index = 0
        return self.decode(s)
    
    def decode(self, s):
        number = 0
        word = ''
        while self.index < len(s):
            c = s[self.index]
            if c.isdigit():
                number = number * 10 + int(c)
            elif c.isalpha():
                word += c
            elif c == '[':
                self.index += 1
                word += number * self.decode(s)
                number = 0
            else: # c == ']'
                return word
            self.index += 1
        return word
                

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