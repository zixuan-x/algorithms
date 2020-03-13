# BFS one time, start from edge
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0]) if m else 0
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
                    queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            board[x][y] = 'D'
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if x + dx >= 0 and x + dx < m and y + dy > 0 and y + dy < n and board[x + dx][y + dy] == 'O':
                    queue.append((x + dx, y + dy))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'D':
                    board[i][j] = 'O'

# DFS one time, start from edge
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0]) if m else 0
        for i in range(m):
            for j in range(n):
                if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
                    self.mark( board, i, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                
    def mark(self, board, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return 
        else:
            board[i][j] = 'D'
            self.mark(board, i + 1, j, m, n)
            self.mark(board, i - 1, j, m, n)
            self.mark(board, i, j + 1, m, n)

# DFS two times
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0]) if n else 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if self.dfs(board, i, j, n, m, set()):
                        self.mark(board, i, j, n, m)
    
    def dfs(self, board, i, j, n, m, visited):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        elif (i, j) in visited or board[i][j] == 'X':
            return True
        else:
            visited.add((i, j))
            return self.dfs(board, i + 1, j, n, m, visited) and self.dfs(board, i - 1, j, n, m, visited) and self.dfs(board, i, j + 1, n, m, visited) and self.dfs(board, i, j - 1, n, m, visited)

    def mark(self, board, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == 'X':
            return 
        else:
            board[i][j] = 'X'
            self.mark(board, i + 1, j, n, m)
            self.mark(board, i - 1, j, n, m)
            self.mark(board, i, j + 1, n, m)
            self.mark(board, i, j - 1, n, m)