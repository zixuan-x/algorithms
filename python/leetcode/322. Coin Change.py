"""
dp - bottom-up:
[10:22] try to use dp, bottom up approach
use large coins first, or small coins first?
I think shoud be using small coins first, since we are build an array from 0 to amount

[10:23] try to implement
[10:29] solved

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:    
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                         
        return dp[-1] if dp[-1] != float('inf') else -1     
    
'''
memo search - top-down:
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.memoSearch(coins, amount, {})
        
    def memoSearch(self, coins, amount, memo):
        '''
        Returns smallest # of coins needed to make up the amount, -1 if not possible
        '''
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        if amount in memo:
            return memo[amount]
        
        result = float('inf')
        for coin in coins:
            temp = self.memoSearch(coins, amount - coin, memo)
            if temp >= 0:
                result = min(result, temp)
                
        memo[amount] = result + 1 if result != float('inf') else -1
        return memo[amount]

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
class Solution:
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