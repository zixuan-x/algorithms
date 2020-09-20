'''
layer:
space: O(1)
'''
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        result, layer = 0, 0
        for i in range(len(S)):
            if S[i] == '(':
                layer += 1
            else:
                layer -= 1
            if S[i - 1] == '(' and S[i] == ')':
                result += 1 << layer
        return result

'''
stack:
space: O(n)
'''
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        cur = 0
        for c in S:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = stack.pop() + (1 if cur == 0 else 2 * cur)
        return cur

'''
recursion:
'''
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        self.index = 0
        return self.getScore(S)
        
    def getScore(self, S):
        result = 0
        while self.index < len(S):
            c = S[self.index]
            self.index += 1
            if c == '(':
                if S[self.index] == ')':
                    result += 1
                    self.index += 1
                else:
                    result += 2 * self.getScore(S)                
            else: # c == ')'
                return result
        return result