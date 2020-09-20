class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        invalids = set(stack)
        result = []
        for i in range(len(s)):
            if i in invalids:
                continue
            result.append(s[i])
        return ''.join(result)