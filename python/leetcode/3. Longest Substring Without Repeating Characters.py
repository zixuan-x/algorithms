class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        chars = {}
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in chars:
                left = max(left, chars[c] + 1)
            chars[c] = right
            length = max(length, right - left + 1)
        return length