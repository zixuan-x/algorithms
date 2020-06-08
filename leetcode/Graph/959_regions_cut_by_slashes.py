class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parents = [i for i in range(4 * n * n)]
        ranks = [1 for i in range(4 * n * n)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
            
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if px < py:
                parents[px] = py
            elif px > py:
                parents[py] = px
            else:
                parents[px] = py
                ranks[py] += 1
                
        for r in range(n):
            for c in range(n):
                index = 4 * (r * n + c)
                if grid[r][c] == '/':
                    union(index + 0, index + 3)
                    union(index + 1, index + 2)
                elif grid[r][c] == '\\':
                    union(index + 0, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index + 0, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)
                if r + 1 < n:
                    union(index + 2, index + 4 * n + 0)
                if c + 1 < n:
                    union(index + 1, index + 4 + 3)
        
        count = 0
        for i in range(4 * n * n):
            if parents[i] == i:
                count += 1
        return count