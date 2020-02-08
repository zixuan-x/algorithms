class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(res)
                res = ""
            elif s[i] == ')':
                res = stack.pop() + res[::-1]
            else:
                res += s[i]
        
        return res