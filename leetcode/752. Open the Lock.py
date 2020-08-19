class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([('0000', 0)])
        visited = set([('0000')])
        while queue:
            cur, count = queue.popleft()
            if cur == target:
                return count
            if cur in deadends:
                continue
            for i in range(4):
                n = int(cur[i])
                for move in [1, 9]:
                    s = cur[:i] + str((n + move) % 10) + cur[i + 1:]
                    if s not in visited:
                        visited.add(s)
                        queue.append((s, count + 1))
        return -1