class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        value = 1 if player == 1 else -1
        self.rows[row] += value
        self.cols[col] += value
        
        
        
        if row == col:
            self.diagonal += value
            
        if row + col == self.size - 1:
            self.antiDiagonal += value
            
        if abs(self.rows[row]) == self.size or abs(self.cols[col]) == self.size or abs(self.diagonal) == self.size or abs(self.antiDiagonal) == self.size:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)