class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict: return []
        wordDict = set(wordDict)
        m = len(max(wordDict, key=len))
        return self.memoSearch(s, wordDict, {}, m)
    
    def memoSearch(self, s, wordDict, memo, m):
        if len(s) == 0:
            return []
        
        if s not in memo:
            partitions = []
            for i in range(min(m, len(s))):
                prefix = s[:i+1]
                if prefix not in wordDict:
                    continue
                
                subPartitions = self.memoSearch(s[i+1:], wordDict, memo, m)
                for subPartition in subPartitions:
                    partitions.append(prefix + ' ' + subPartition)
            
            if s in wordDict:
                partitions.append(s)
                
            memo[s] = partitions
        
        return memo[s]
