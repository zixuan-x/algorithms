from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        buildings = sum(1 if grid[i][j] == 1 else 0 for i in range(m) for j in range(n))
        
        distance = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, distance, reach)
        
        minDistance = float('inf')
        for i in range(m):
            for j in range(n):
                if reach[i][j] == buildings and distance[i][j] < minDistance:
                    minDistance = distance[i][j]
        return minDistance if minDistance != float('inf') else -1
    
    def bfs(self, grid, i, j, distance, reach):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque([(i, j, 0)])
        while queue:
            x, y, d = queue.popleft()
            if not visited[x][y]:
                visited[x][y] = True
                if grid[x][y] == 0:
                    reach[x][y] += 1
                    distance[x][y] += d
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (0 <= x + dx < m) and (0 <= y + dy < n) and grid[x + dx][y + dy] == 0:
                        queue.append((x + dx, y + dy, d + 1))
        