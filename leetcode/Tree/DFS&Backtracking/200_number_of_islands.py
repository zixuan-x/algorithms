class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        
        row = len(grid)
        column = len(grid[0])
        
        islands = 0
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    islands += 1
                    self.mark_zero(grid, i, j)
                    
        return islands
    
    def mark_zero(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '#'
        self.mark_zero(grid, i + 1, j)
        self.mark_zero(grid, i - 1, j)
        self.mark_zero(grid, i, j + 1)
        self.mark_zero(grid, i, j - 1)