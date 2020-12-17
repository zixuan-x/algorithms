class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d > target or d <= 0:
            return 0
        return self.memoSearch(d, f, target, {}) % (10 ** 9 + 7)
        
        
    def memoSearch(self, d, f, t, memo):
        if d == 1:
            return int(0 < t <= f)
        
        if (d, t) in memo:
            return memo[(d, t)]
        
        ways = 0
        for i in range(1, f + 1):
            ways += self.memoSearch(d - 1, f, t - i, memo)
        memo[(d, t)] = ways
        return ways
        
        