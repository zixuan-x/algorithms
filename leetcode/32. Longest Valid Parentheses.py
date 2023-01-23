class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == ')' and len(stack) > 1 and s[stack[-1]] == '(':
                stack.pop()
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)
        
        return max_len

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == ')' and len(stack) > 1 and s[stack[-1]] == '(':
                stack.pop()
            else:
                max_len = max(max_len, i - stack[-1] - 1)
                stack.append(i)    
        max_len = max(max_len, len(s) - stack[-1] - 1)
        return max_len

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, c in enumerate(s):
            if c == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        
        max_len, pre = 0, -1
        stack.append(len(s))
        for i in range(len(stack)):
            max_len = max(max_len, stack[i] - pre - 1)
            pre = stack[i]
        
        return max_len