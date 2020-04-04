from heapq import heappush, heappop

# Dijkstra' Algorithm only works for graphs with non-negative edge weights.

# graph is type {int: list}, start and end are integers. return type : int
def dijkastra(graph, start, end):
    """Dijkastra (Start to End)"""
    heap = [(0, start)] # (dist, node)
    visited = set()
    while heap:
        distance, node = heappop(heap)
        if node == end:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor, d in graph[node]:
                heappush(heap, (distance + d, neighbor))
    return -1

# graph is type {int: list}, start is type int. return type : {int: int}
def dijkastra(graph, start):
    """Dijkastra (All Shortest Paths)"""
    heap = [(0, start)] # (dist, node)
    visited = {} # {node: distance}
    while heap:
        distance, node = heappop(heap)
        if node not in visited:
            visited[node] = distance
            for neighbor, d in graph[node]:
                heappush(heap, (distance + d, neighbor))
    return visited
