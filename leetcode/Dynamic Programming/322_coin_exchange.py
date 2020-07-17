class Solution:
    """
    [10:22] try to use dp, bottom up approach
    use large coins first, or small coins first?
    I think shoud be using small coins first, since we are build an array from 0 to amount
    
    [10:23] try to implement
    [10:29] solved
    
    """
    def coinChange(self, coins: List[int], amount: int) -> int:    
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[-1] if dp[-1] != float('inf') else -1
                
    
    
    """
    1. each level represent a type of coin
    2. there are n levels where n == len(coins)
    3. each branch represents how many that type of coin we wiil choose
            0
           / \
    1:    0 1 2  3 4 5
    2: 
    5: 
    
    [10:22] failed due to time limit
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest = [float("inf")]
        self.dfs(coins, amount, 0, 0, fewest, 0)
        return fewest[0] if fewest[0] != float("inf") else -1
        
    def dfs(self, coins, amount, curSum, curNum, fewest, index):
        if index >= len(coins) or curSum >= amount:
            if curSum == amount:
                fewest[0] = min(fewest[0], curNum)
                return
        else:
            for i in range((amount - curSum) // coins[index] + 1):
                self.dfs(coins, amount, curSum + i * coins[index], curNum + i, fewest, index + 1)
            