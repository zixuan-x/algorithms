from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        queue = deque([('0000', 0)])
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            if lock in visited or lock in deadends:
                continue
            visited.add(lock)
            for i in range(4):
                n = int(lock[i])
                queue.append((lock[:i] + str((n + 1) % 10) + lock[i + 1:], turns + 1))
                queue.append((lock[:i] + str((n - 1 + 10) % 10) + lock[i + 1:], turns + 1))
        return -1