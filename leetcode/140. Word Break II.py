class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        
        wordDict = set(wordDict)
        m = len(max(wordDict, key=len))
        return self.memoSearch(s, wordDict, m, {})
        
    def memoSearch(self, s, wordDict, m, memo):
        if not s:
            return []
        
        # a word may be divided into other words!
        # if s in wordDict:
        #     return [s]
        
        if s in memo:
            return memo[s]
        
        sentences = []
        for i in range(min(len(s), m)):
            substring = s[:i + 1]
            if substring not in wordDict:
                continue
            for subsentence in self.memoSearch(s[i + 1:], wordDict, m, memo):
                sentences.append(substring + ' ' + subsentence)
        
        if s in wordDict:
            sentences.append(s)
        
        memo[s] = sentences
        return sentences
            
        