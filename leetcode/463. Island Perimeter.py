class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                        count += 1
        return count



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return self.search(grid, i, j, m, n)
        
    def search(self, grid, i, j, m, n):
        queue = deque([(i, j)])
        visited = set([(i, j)])
        count = 0
        while queue:
            x, y = queue.popleft()
            peri = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (x + dx) < 0 or (x + dx) >= m or (y + dy) < 0 or (y + dy) >= n or grid[x + dx][y + dy] == 0 or (x + dx, y + dy) in visited:
                    peri += 1
                    if (x + dx, y + dy) in visited:
                        peri -= 1
                    continue
                visited.add((x + dx, y + dy))
                queue.append((x + dx, y + dy))
            count += peri
        return count
        