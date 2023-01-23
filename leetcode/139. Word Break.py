'''
1. memoization search - top down

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return True
        if not wordDict: return False
        
        wordDict = set(wordDict)
        m = len(max(wordDict, key=len))
        return self.memoSearch(s, wordDict, {}, m)
        
    def memoSearch(self, s, wordDict, memo, m):
        # base case
        if not s or s in wordDict:
            return True
        
        # recursive rules
        if s not in memo:
            isValid = False
            for i in range(min(m, len(s))):
                if s[:i+1] in wordDict and self.memoSearch(s[i+1:], wordDict, memo, m):
                    isValid = True
                    break
            memo[s] = isValid
        return memo[s]


'''
2. dynamic programming - bottom up

'''
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
                