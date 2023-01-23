class Solution:
    '''
    1. dp[i][j] = minimum path sum from (0, 0) to (i, j)
    2. dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    3. dp[0][0] = grid[0][0]
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i - 1 < 0 and j - 1 < 0:
                    dp[i][j] = grid[i][j]
                elif i - 1 < 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j - 1 < 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[-1][-1]
                
                