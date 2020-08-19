'''
1. 
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.getScore(piles, 0, len(piles) - 1)
    
    def getScore(self, piles, l, r):
        if l == r:
            return piles[l]
        
        return max(piles[l] - self.getScore(piles, l + 1, r), piles[r] - self.getScore(piles, l, r - 1))
        

'''
2. 
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.getScore(piles, 0, len(piles) - 1, {}) > 0
    
    def getScore(self, piles, l, r, memo):
        if l == r:
            return piles[l]
        
        if (l, r) not in memo:
            memo[(l, r)] = max(piles[l] - self.getScore(piles, l + 1, r, memo), piles[r] - self.getScore(piles, l, r - 1, memo))
        
        return memo[(l, r)]
        