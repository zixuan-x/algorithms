class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return not word
        if len(board) * len(board[0]) < len(word):
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, 0, i, j, set()):
                    return True
        return False
        
    def search(self, board, word, index, i, j, visited):
        if index == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[index] != board[i][j]:
            return False
        
        visited.add((i, j))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (i + dx, j + dy) not in visited and self.search(board, word, index + 1, i + dx, j + dy, visited):
                return True
        visited.remove((i, j))
        return False