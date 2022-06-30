from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        maxLength, head = float('inf'), 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
            
            while missing == 0:
                if right - left + 1 < maxLength:
                    maxLength = right - left + 1
                    head = left
                c = s[left]
                if c in need:
                    if need[c] >= 0:
                        missing += 1
                    need[c] += 1
                left += 1
        return s[head: head + maxLength] if maxLength != float('inf') else ''