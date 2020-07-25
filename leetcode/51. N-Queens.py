class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        self.search(0, n, [], results)
        print(results)
        return self.drawChessboard(n, results)
        
    def search(self, row, n, cols, results):
        if row == n:
            results.append(cols[:])
            return
        
        for col in range(n):
            if not self.isValid(row, col, cols):
                continue
            cols.append(col)
            self.search(row + 1, n, cols, results)
            cols.pop()
            
    def isValid(self, row, col, cols):
        for r, c in enumerate(cols):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True
    
    def drawChessboard(self, n, results):
        boards = []
        for cols in results:
            board = []
            for i in range(n):
                board.append('.' * cols[i] + 'Q' + '.' * (n - cols[i] - 1))
            boards.append(board)
        return boards