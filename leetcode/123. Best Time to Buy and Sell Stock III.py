class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        K = 2
        
        dp = [[0] * n for _ in range(K + 1)]
        
        for k in range(1, K + 1):
            maxDiff = float('-inf')
            for i in range(1, n):
                maxDiff = max(maxDiff, dp[k - 1][i - 1] - prices[i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] + maxDiff)
        return dp[K][-1]
            
        
        