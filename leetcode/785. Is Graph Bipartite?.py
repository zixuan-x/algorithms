from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] != 0:
                continue
            queue = deque([(i, 1)])
            while queue:
                node, flag = queue.popleft()
                if colors[node] != 0 and flag != colors[node]:
                    return False
                if colors[node] == 0:
                    colors[node] = flag
                    for neighbor in graph[node]:
                        queue.append((neighbor, -flag))
        return True