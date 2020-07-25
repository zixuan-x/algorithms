from collections import deque

class Solution:
    """
    1. DFS, iterate through all points, and for every point, try if it can flow to both ways
    Time Complexity: O(m * n * m * n)
    Space Complexity: O(1) without counting stack
    
    2. DFS/BFS flow from border
        (When using search algo's, think if you can swap start and end points)
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    
    3. dp-like solution
        two matrix to track if a point can go to pacific/atlantic
        if one can reach pacific, nearby higher point can reach pacific too
    """
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        for x in range(m):
            self.dfs(matrix, x, 0, 0, pacific)
            self.dfs(matrix, x, n - 1, 0, atlantic)
            
        for y in range(n):
            self.dfs(matrix, 0, y, 0, pacific)
            self.dfs(matrix, m - 1, y, 0, atlantic)
        
        res = []
        for x in range(m):
            for y in range(n):
                if pacific[x][y] and atlantic[x][y]:
                    res.append([x, y])
        return res
    
    def dfs(self, matrix, x, y, h, ocean):
        if x < 0 or x >= len(ocean) or y < 0 or y >= len(ocean[0]) or ocean[x][y] or matrix[x][y] < h: 
            return
        else:
            ocean[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.dfs(matrix, x + dx, y + dy, matrix[x][y], ocean)

''' 2. BFS '''
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        graph = [[0] * n for _ in range(m)]
        
        # search Pacific
        queue = deque()
        for i in range(m):
            queue.append((i, 0))
        for j in range(1, n):
            queue.append((0, j))
        self.bfs(matrix, graph, queue, 1)
        
        # search Atlantic
        queue = deque()
        for i in range(m):
            queue.append((i, n - 1))
        for j in range(n - 1):
            queue.append((m - 1, j))
        self.bfs(matrix, graph, queue, 2)
        
        # find results
        results = []
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 3:
                    results.append([i, j])
        return results
        
    def bfs(self, matrix, graph, queue, token):
        m, n = len(matrix), len(matrix[0])
        visited = set()
        while queue:
            x, y = queue.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                graph[x][y] += token
                for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    if (0 <= x + dx < m) and (0 <= y + dy < n) and matrix[x + dx][y + dy] >= matrix[x][y]:
                        queue.append((x + dx, y + dy))