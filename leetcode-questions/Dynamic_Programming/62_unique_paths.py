class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0] * n for _ in range(m)]
        board[0][0] = 1
        for i in range(m):
            for j in range(n):
                left = board[i][j - 1] if j > 0 else 0
                up = board[i - 1][j] if i > 0 else 0
                board[i][j] += left + up
        
        return board[-1][-1]