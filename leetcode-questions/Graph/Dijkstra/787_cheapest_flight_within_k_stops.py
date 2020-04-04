from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        Since the shortest path may not be within K stops, we must not maintain a visited set.
        Instead, we need to search all possible paths within K stops.
        Therefore, we allow revisiting nodes.
        """
        # adjacency list
        graph = defaultdict(list) # {node: [(node, cost)]}
        for start, end, cost in flights:
            graph[start].append((end, cost))
        
        heap = [(0, src, -1)] # [(cost, node, steps)]
        while heap:
            cost, node, steps = heappop(heap)
            if node == dst:
                return cost
            if steps < K:
                for neighbor, price in graph[node]:
                    heappush(heap, (cost + price, neighbor, steps + 1))
        return -1
        
        