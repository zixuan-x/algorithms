class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        results = []
        left, right =  self.calcUnmatched(s)
        self.search(s, 0, left, right, results)
        return results
        
    def search(self, s, start, left, right, results):
        if left == 0 and right == 0:
            if self.isValid(s):
                results.append(s)
            return
        
        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            if s[i] == '(':
                self.search(s[:i]+s[i+1:], i, left-1, right, results)
            if s[i] == ')':
                self.search(s[:i]+s[i+1:], i, left, right-1, results)
    
    def calcUnmatched(self, s):
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right
            
    def isValid(self, s):
        left, right = self.calcUnmatched(s)
        return left == 0 and right == 0
        