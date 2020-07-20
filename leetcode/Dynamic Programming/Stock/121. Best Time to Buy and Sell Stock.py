class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, profit = float('inf'), 0
        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            profit = max(profit, prices[i] - lowest)
        return profit