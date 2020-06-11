class Solution:
    def reverseParentheses(self, s: str) -> str:
        cur = ''
        stack = []
        for c in s:
            if c == '(':
                stack.append(cur)
                cur = ''
            elif c == ')':
                cur = stack.pop() + cur[::-1]
            else:
                cur += c
        return cur