class Solution:
    """
    [2:48] start
    dp(i) -> prev min & maxProfit
    """
    def maxProfit(self, prices: List[int]) -> int:
        lowest, maxProfit = float('inf'), 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return maxProfit