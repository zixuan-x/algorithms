class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return rooms
        MAXINTEGER = 2147483647
        m, n = len(rooms), len(rooms[0])
        queue = deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
        # 因为queue里面存的全是0，所以第一波被push进queue的全是离各个gate最近的room，因此并不需要重复访问同一个room
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                if r < 0 or r >= m or c < 0 or c >= n or rooms[r][c] != MAXINTEGER:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))
        
                