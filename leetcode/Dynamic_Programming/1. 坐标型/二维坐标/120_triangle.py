# 1. DFS bottom-up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = [float('inf')]
        self.dfs(triangle, 0, 0, 0, res)
        return res[0]
    
    def dfs(self, triangle, x, y, path_sum, res):
        if x == len(triangle):
            res[0] = min(res[0], path_sum)
            return
        
        self.dfs(triangle, x + 1, y, path_sum + triangle[x][y], res)
        self.dfs(triangle, x + 1, y + 1, path_sum + triangle[x][y], res)

# 2. DFS top-down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.dfs(triangle, 0, 0)
        
    def dfs(self, triangle, x, y):
        if x == len(triangle):
            return 0
        
        left = self.dfs(triangle, x + 1, y)
        right = self.dfs(triangle, x + 1, y + 1)
        return min(left, right) + triangle[x][y]

# 3. DP Memoization Search top-down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.dfs(triangle, 0, 0, {})
        
    def dfs(self, triangle, x, y, memo):
        # base case
        if x == len(triangle):
                return 0

        # if not computed
        if (x, y) not in memo:
            left = self.dfs(triangle, x + 1, y, memo)
            right = self.dfs(triangle, x + 1, y + 1, memo)

            # remember current calculation
            memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]

# 4. DP Iterative top-down O(n^2) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        
        n = len(triangle)
        
        # allocate dp array
        dp = [[0] * (i + 1) for i in range(n)]
        
        # base case initialization
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        
        # state transition
        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        
        return min(dp[n - 1])

# 5. DP Iterative bottom-up O(n^2) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        
        n = len(triangle)
        
        # allocate dp array
        dp = [[0] * (i + 1) for i in range(n)]
        
        # base case initialization
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]
        
        # state transition
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        
        return dp[0][0]

# 6. DP Iterative bottom-up O(n) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        
        n = len(triangle)
        
        # allocate dp array
        dp = [[0] * n, [0] * n]
        
        # base case initialization
        for i in range(n):
            dp[(n - 1) % 2][i] = triangle[n - 1][i]
        
        # state transition
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i % 2][j] = min(dp[(i + 1) % 2][j], dp[(i + 1) % 2][j + 1]) + triangle[i][j]
        
        return dp[0][0]
        