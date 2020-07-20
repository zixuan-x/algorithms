class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2: return 0
        profit = 0
        min_available = prices[0]
        for i in range(1, n):
            if prices[i] < min_available:
                min_available = prices[i]
            elif prices[i] > min_available + fee:
                profit += prices[i] - min_available - fee
                min_available = prices[i] - fee
        return profit
            
        
        