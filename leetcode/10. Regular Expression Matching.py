class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.memoSearch(s, p, 0, 0, {})
        
    def memoSearch(self, s, p, i, j, memo):
        # base cases
        if i == len(s):
            return self.isEmpty(p[j:])
        if j == len(p):
            return False
        
        # already computed
        if (i, j) in memo:
            return memo[(i, j)]
               
        # not computed yet
        if j + 1 < len(p) and p[j + 1] == '*':
            return self.memoSearch(s, p, i, j + 2, memo) or (self.isCharMatched(s[i], p[j]) and self.memoSearch(s, p, i + 1, j, memo))
        else:
            return self.isCharMatched(s[i], p[j]) and self.memoSearch(s, p, i + 1, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched
    
    def isCharMatched(self, s, p):
        return s == p or p == '.'
    
    def isEmpty(self, p):
        if len(p) % 2 != 0:
            return False
        
        for i in range(len(p) // 2):
            if p[i * 2 + 1] != '*':
                return False
        
        return True
        
        