from collections import deque

class Solution:
    """
    1. DFS - O(n ^ 2)
    Note: 数组元素是string，不是int
    """
    def numIslands1(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
    
        return count
    
    def dfs(self, grid, i, j):
        if not grid or not grid[0]: return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0': return
        
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
    
    """
    2. BFS - O(n ^ 2)
    """
    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)
    
        return count
    
    def bfs(self, grid, i, j):
        if not grid or not grid[0]: return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0': return
        
        queue = deque([(i, j)])
        grid[i][j] = '0'
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if x + dx >= 0 and x + dx < len(grid) and y + dy >= 0 and y + dy < len(grid[0]) and grid[x + dx][y + dy] == '1':
                    grid[x + dx][y + dy] = '0'
                    queue.append((x + dx, y + dy))


    """
    3. Union Find - O(n ^ 2)
    
    """