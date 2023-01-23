import sys
from heapq import heappush, heappop
from collections import defaultdict


def dijkstra(edges: list[list[int]], src: int, dst: int, n: int) -> int:
    graph = build_graph(edges)  # {node: [(neighbor, cost)..]}

    distances = [sys.maxsize] * n  # or [float("int")] * n

    minHeap = [(0, src)]
    while minHeap:
        distance, cur = heappop(minHeap)
        if distances[cur] < sys.maxsize:
            continue
        distances[cur] = distance

        for neighbor, cost in graph[cur]:
            if distances[neighbor] < sys.maxsize:
                continue
            heappush(minHeap, (distance + cost, neighbor))

    return distances[dst] if distances[dst] < float("inf") else -1


def build_graph(edges):
    graph = defaultdict(list)  # {node: [(neighbor, cost)..]}
    for src, dst, cost in edges:
        graph[src].append((dst, cost))
    return graph


def dijkstra_2(edges: list[list[int]], src: int, dst: int, n: int) -> int:
    graph = build_graph(edges)  # {node: [(neighbor, cost)..]}

    distances = [sys.maxsize] * n  # or [float("int")] * n
    distances[src] = 0

    minHeap = [(0, src)]
    visited = set()
    while minHeap:
        distance, cur = heappop(minHeap)
        if cur in visited:
            continue
        visited.add(cur)

        for neighbor, cost in graph[cur]:
            if neighbor in visited:
                continue
            new_distance = distance + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(minHeap, (new_distance, neighbor))

    if len(visited) != len(distances):
        return -1
    return distances[dst]
