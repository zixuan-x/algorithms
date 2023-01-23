from collections import deque

"""
1. DFS - O(m * n)
Note: 数组元素是string，不是int
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
2. BFS - O(m * n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
3. Union Find - O(m * n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        parents = list(range(m * n))
        ranks = [1] * (m * n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                index = i * n + j
                if j < n - 1 and grid[i][j + 1] == '1':
                    self.union(parents, ranks, index, index + 1)
                if i < m - 1 and grid[i + 1][j] == '1':
                    self.union(parents, ranks, index, index + n)
        
        roots = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                index = i * n + j
                roots.add(self.find(parents, index))
        return len(roots)
        
    
    def find(self, parents, u):
        if u != parents[u]:
            parents[u] = self.find(parents, parents[u])
        return parents[u]
        
        
    def union(self, parents, ranks, u, v):
        ru, rv = self.find(parents, u), self.find(parents, v)
        if ru == rv:
            return False
        
        if ranks[ru] < ranks[rv]:
            parents[ru] = rv
        elif ranks[ru] > ranks[rv]:
            parents[rv] = ru
        else:
            parents[ru] = rv
            ranks[rv] += 1
            
        return True