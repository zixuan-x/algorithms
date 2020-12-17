from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        result = 0
        left, maxFreq = 0, 0
        for right in range(len(s)):
            c = s[right]
            freq[c] += 1
            maxFreq = max(maxFreq, freq[c])
            while right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result