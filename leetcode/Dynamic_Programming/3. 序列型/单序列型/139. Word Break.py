class Solution:
    """
    1. dp(i) -> True if s[0:i] can be segmented into words, otherwise false
    2. dp(i) = True if dp(i - len(word[j])) else False
    3. dp(0) = True
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict: return False
        n = len(s)
        m = len(max(wordDict, key = len))
        dp = [False] * (n + 1)
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(n):
            if not dp[i]: continue
            for j in range(i, min(n, i + m)):
                if s[i:j + 1] in wordSet:
                    dp[j + 1] = True
                if dp[-1]: return True
        return dp[-1]
                