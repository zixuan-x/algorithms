from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        queue = deque([(start[0], start[1])])
        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True
            if (x, y) not in visited:
                visited.add((x, y))
                for i, j in self.getNeighbors(maze, x, y):
                    queue.append((i, j))
        return False

    def getNeighbors(self, maze, x, y):
        neighbors = []
        i = x
        while i - 1 >= 0 and maze[i - 1][y] == 0:
            i -= 1
        neighbors.append((i, y))
        
        i = x
        while i + 1 < len(maze) and maze[i + 1][y] == 0:
            i += 1
        neighbors.append((i, y))
        
        j = y
        while j - 1 >= 0 and maze[x][j - 1] == 0:
            j -= 1
        neighbors.append((x, j))
        
        j = y
        while j + 1 < len(maze[0]) and maze[x][j + 1] == 0:
            j += 1
        neighbors.append((x, j))
        
        return neighbors