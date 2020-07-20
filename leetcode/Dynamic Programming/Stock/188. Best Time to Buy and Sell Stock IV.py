class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        if k >= n // 2:
            maxProfit = 0
            for i in range(1, n):
                maxProfit += max(0, prices[i] - prices[i - 1])
            return maxProfit
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for K in range(1, k + 1):
            maxDiff = float('-inf')
            for i in range(1, n):
                maxDiff = max(maxDiff, dp[K - 1][i - 1] - prices[i - 1])
                dp[K][i] = max(dp[K][i - 1], prices[i] + maxDiff)
        return dp[K][-1]
            