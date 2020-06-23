# Dynamic Programming Solution


# Backtracking Solution
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        r = len(grid)
        c = len(grid[0]) if r else 0
        
        res = [float("inf")]
        path = 0
        
        self.dfs(grid, 0, 0, r, c, path, res)
        
        return res[0]
        
        
    def dfs(self, grid, x, y, r, c, path, res):
        if x < 0 or y < 0 or x >= r or y >= c:
            return
        
        if x == r - 1 and y == c - 1:
            res[0] = min(res[0], path + grid[x][y])
            return
        
        path += grid[x][y]
        self.dfs(grid, x + 1, y, r, c, path, res)
        self.dfs(grid, x, y + 1, r, c, path, res)
        path -= grid[x][y]