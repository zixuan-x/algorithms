from heapq import heappush, heappop

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = set()
        heap = [(0, start[0], start[1])]
        while heap:
            cost, x, y = heappop(heap)
            if [x, y] == destination:
                return cost
            if (x, y) not in visited:
                visited.add((x, y))
                for c, i, j in self.getNeighbors(maze, x, y):
                    heappush(heap, (c + cost, i, j))
        return -1
                
    def getNeighbors(self, maze, x, y):
        neighbors = []
        i = x
        while i - 1 >= 0 and maze[i - 1][y] == 0:
            i -= 1
        neighbors.append((abs(x - i), i, y))
        
        i = x
        while i + 1 < len(maze) and maze[i + 1][y] == 0:
            i += 1
        neighbors.append((abs(x - i), i, y))
        
        j = y
        while j - 1 >= 0 and maze[x][j - 1] == 0:
            j -= 1
        neighbors.append((abs(y - j), x, j))
        
        j = y
        while j + 1 < len(maze[0]) and maze[x][j + 1] == 0:
            j += 1
        neighbors.append((abs(y - j), x, j))
        
        return neighbors
        