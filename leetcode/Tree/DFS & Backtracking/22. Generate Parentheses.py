class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.search(n, n, [], results)
        return results
    
    def search(self, left, right, path, results):
        if left == 0 and right == 0:
            results.append(''.join(path))
            return
        
        if left > 0:
            path.append('(')
            self.search(left - 1, right, path, results)
            path.pop()
            
        if left < right:
            path.append(')')
            self.search(left, right - 1, path, results)
            path.pop()