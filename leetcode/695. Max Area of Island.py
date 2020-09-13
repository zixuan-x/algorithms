class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        result = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    result = max(result, self.search(grid, i, j, visited))
        return result
    
    def search(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j)])
        count = 0
        while queue:
            r, c = queue.popleft()
            if (r, c) not in visited:
                count += 1
                print(r, c, count)
                visited.add((r, c))
                for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 1 or (nr, nc) in visited:
                        continue
                    queue.append((nr, nc))
        return count

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        result = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    result = max(result, self.search(grid, i, j, visited))
        return result
    
    def search(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j)])
        visited.add((i, j))
        # count = 0
        count = 1
        while queue:
            r, c = queue.popleft()
            # if (r, c) in visited:
            #     continue
            # count += 1
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 1 or (nr, nc) in visited:
                    continue
                count += 1
                visited.add((nr, nc))
                queue.append((nr, nc))
        return count