class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in mapping: # closing
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else: # opening
                stack.append(c)
        return not stack
                