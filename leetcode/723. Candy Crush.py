class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])
        while True:
            # crush adjacent elements
            crushed = set()          
            for i in range(m):
                for j in range(n):
  
                    if board[i][j] == 0:
                        continue
                    
                    # crush horizontally
                    if j < n - 2 and board[i][j + 1] == board[i][j + 2] == board[i][j]:
                        crushed |= {(i, j), (i, j + 1), (i, j + 2)}
                        
                    # crush vertically
                    if i < m - 2 and board[i + 1][j] == board[i + 2][j] == board[i][j]:
                        crushed |= {(i, j), (i + 1, j), (i + 2, j)}
            
            if not crushed:
                break
                
            for i, j in crushed:
                board[i][j] = 0
            
            # update board
            for j in range(n):
                bottom = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] > 0:
                        board[bottom][j] = board[i][j]
                        bottom -= 1
                for i in range(bottom, -1, -1):
                    board[i][j] = 0
            
        return board



'''
Couldn't pass one test case
'''
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board or not board[0]:
            return board
        m, n = len(board), len(board[0])
        crushed = True
        while crushed:
            crushed = False
            
            # crush adjacent elements
            for i in range(m):
                for j in range(n):
                    val = abs(board[i][j])
                    if val == 0:
                        continue
                        
                    # crush vertically
                    if not (i > 0 and board[i - 1][j] == -val):
                        if i < m - 2 and abs(board[i + 1][j] == val and abs(board[i + 2][j]) == val):
                            crushed = True
                            index = i
                            while index < m and abs(board[index][j]) == val:
                                board[index][j] = -val
                                index += 1
                    
                    # crush horizontally
                    if not (j > 0 and board[i][j - 1] == -val):
                        if j < n - 2 and abs(board[i][j + 1] == val and abs(board[i][j + 2]) == val):
                            crushed = True
                            index = j
                            while index < n and abs(board[i][index]) == val:
                                board[i][index] = -val
                                index += 1
            
            # update board
            if crushed:
                for j in range(n):
                    bottom = m - 1
                    for i in range(m - 1, -1, -1):
                        if board[i][j] > 0:
                            board[bottom][j] = board[i][j]
                            bottom -= 1
                    for k in range(bottom, -1, -1):
                        board[k][j] = 0
            
            
        return board