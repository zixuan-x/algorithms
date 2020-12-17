class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        turns = 0
        xwin, owin = False, False
        rows, cols = [0] * 3, [0] * 3
        diagonal, antiDiagonal = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    turns += 1; rows[i] += 1; cols[j] += 1
                    if i == j:
                        diagonal += 1
                    if i + j == 2:
                        antiDiagonal += 1
                elif board[i][j] == 'O':
                    turns -= 1; rows[i] -= 1; cols[j] -= 1
                    if i == j:
                        diagonal -= 1
                    if i + j == 2:
                        antiDiagonal -= 1
        xwin = any([rows[i] == 3 for i in range(3)] + [cols[j] == 3 for j in range(3)] + [diagonal == 3, antiDiagonal == 3])
        
        owin = any([rows[i] == -3 for i in range(3)] + [cols[j] == -3 for j in range(3)] + [diagonal == -3, antiDiagonal == -3])
        
        if (xwin and turns != 1) or (owin and turns != 0):
            return False
        
        return turns in (0, 1) and not (xwin and owin)