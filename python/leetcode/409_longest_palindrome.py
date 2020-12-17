class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        else:
            count = 0
            c_set = set()
            for c in s:
                if c in c_set:
                    c_set.remove(c)
                    count += 2
                else:
                    c_set.add(c)
            return count + 1 if len(c_set) > 0 else count