class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in p.values():
                stack.append(c)
            elif not stack or stack.pop() != p[c]:
                return False

        return stack == []
