class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isRowValid(board, i) or not self.isColumnValid(board, i) or not self.isSubValid(board, (i // 3) * 3, (i % 3) * 3):
                return False
        return True
        
        
    def isRowValid(self, board, row):
        visited = set()
        for num in board[row]:
            if num in visited:
                return False
            elif num.isdigit():
                visited.add(num)
        return True
        
    def isColumnValid(self, board, column):
        visited = set()
        for i in range(9):
            if board[i][column] in visited:
                return False
            elif board[i][column].isdigit():
                visited.add(board[i][column])
        return True
        
    def isSubValid(self, board, i, j):
        visited = set()
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                if board[r][c] in visited:
                    return False
                elif board[r][c].isdigit():
                    visited.add(board[r][c])
        return True