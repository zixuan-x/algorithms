class Solution:
    """
    0
   / \ 
  1   2
     / \
    3   4
    """
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        queue = collections.deque([0])
        visited[0] = True
        
        while queue:
            cur = queue.popleft()
            for i in rooms[cur]:
                if visited[i]: continue
                visited[i] = True
                queue.append(i)
        
        return all(visited)
        