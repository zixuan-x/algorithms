class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list) # {node:[(node, time)]}
        for start, end, time in times:
            graph[start].append((end, time))
        visited = {} # {node: time from src}
        
        heap = [(0, K)] # (time, node)
        while heap:
            time, node = heapq.heappop(heap)
            if node not in visited:
                visited[node] = time
                for neighbor, t in graph[node]:
                    heapq.heappush(heap, (time + t, neighbor))
        return max(visited.values()) if len(visited) == N else -1