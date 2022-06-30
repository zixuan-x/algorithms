from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        counter = Counter(s)
        if all(counter[char] >= k for char in counter):
            return len(s)
        
        result = 0
        left, right = 0, 0
        while right < len(s):
            if counter[s[right]] < k:
                result = max(result, self.longestSubstring(s[left:right], k))
                left = right + 1
            right += 1
        result = max(result, self.longestSubstring(s[left:], k))
        return result        