from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = [False] * len(rooms)
        while queue:
            room = queue.popleft()
            if not visited[room]:
                visited[room] = True
                for neighbor in rooms[room]:
                    queue.append(neighbor)
        return all(visited)