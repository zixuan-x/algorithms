from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set((start[0], start[1]))
        queue = deque([start])
        while queue:
            i, j = queue.popleft()
            for x, y in self.getNeighbors(maze, i, j):
                if (x, y) not in visited:
                    visited.add((x, y))
                    if [x, y] == destination: return True
                    queue.append([x, y])
        
        return False
    
    def getNeighbors(self, maze, x, y):
        neighbors = []
        i = x
        while i - 1 >= 0 and maze[i - 1][y] == 0:
            i -= 1
        neighbors.append([i, y])
            
        i = x
        while i + 1 < len(maze) and maze[i + 1][y] == 0:
            i += 1
        neighbors.append([i, y])
        
        j = y
        while j - 1 >= 0 and maze[x][j - 1] == 0:
            j -= 1
        neighbors.append([x, j])
         
        j = y
        while j + 1 < len(maze[0]) and maze[x][j + 1] == 0:
            j += 1
        neighbors.append([x, j])
        
        return neighbors