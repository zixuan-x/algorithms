class Solution:
    """
            []
        /  |   |  \
      0x1 1x1 2x1 3x1  
      
    """
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n ** .5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for s in range(1, n + 1):
            for square in squares:
                if s - square >= 0:
                    dp[s] = min(dp[s], dp[s - square] + 1)
                else:
                    break
        return dp[-1]