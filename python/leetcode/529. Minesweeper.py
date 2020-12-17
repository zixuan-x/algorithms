from collections import deque

'''
This is a typical Search problem, either by using DFS or BFS. Search rules:

1. If click on a mine ('M'), mark it as 'X', stop further search.
2. If click on an empty cell ('E'), depends on how many surrounding mine:
    2.1 Has surrounding mine(s), mark it with number of surrounding mine(s), stop further search.
    2.2 No surrounding mine, mark it as 'B', continue search its 8 neighbors.
'''
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board
        m, n = len(board), len(board[0])
        row, col = click
        # term: check is mine
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
    
        # Breadth-first Search
        visited = set()
        queue = deque([(row, col)])
        while queue:
            row, col = queue.popleft()
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            # term:  count has nearby mines
            nearbyMines = self.countNearbyMines(board, row, col)
            if nearbyMines > 0: # stop if there are mines nearby
                board[row][col] = str(nearbyMines)
                continue
            
            board[row][col] = 'B'
    
            # propagate otherwise
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    r, c = row + dr, col + dc
                    if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'E':
                        continue
                    queue.append((r, c))
        
        return board
                
    def countNearbyMines(self, board, row, col):
        m, n = len(board), len(board[0])
        nearbyMines = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                if board[r][c] in ['M', 'X']:
                    nearbyMines += 1
        return nearbyMines
                
            