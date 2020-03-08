class Solution:
    """
    [3:28] start
    dp(s, t[:i]) -> how many characters matched
    [3:37] solved
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        matched = 0
        for i in range(len(t)):
            if matched == len(s):
                return True
            if s[matched] == t[i]:
                matched += 1
        return matched == len(s)