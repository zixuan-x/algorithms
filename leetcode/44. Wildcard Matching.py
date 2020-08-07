class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.memoSearch(s, p, {})
        
    def memoSearch(self, s, p, memo):
        if not s:
            if p:
                for c in p:
                    if c != '*':
                        return False
                return True
            else:
                return True
        elif not p:
            return False
            
        
        if (s, p) in memo:
            return memo[(s, p)]
        
        isValid = False
        c1, c2 = s[0], p[0]
        if c2 == '?':
            isValid = self.memoSearch(s[1:], p[1:], memo)
        elif c2 == '*':
            isValid = self.memoSearch(s, p[1:], memo) or self.memoSearch(s[1:], p, memo)
        else:
            isValid = (c1 == c2) and self.memoSearch(s[1:], p[1:], memo)
        
        memo[(s, p)] = isValid
        return isValid
