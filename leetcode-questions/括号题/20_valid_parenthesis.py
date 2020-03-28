class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        left = set(['(', '{', '['])
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False
        
        return len(stack) == 0
        