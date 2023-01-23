from collections import deque, defaultdict
from typing import List, Dict


def topological_sort(vertices: int, edges: List[List[int]]) -> List[int]:
    order = []
    if vertices <= 0:
        return order

    graph = build_graph(vertices, edges)  # {node: [neighbors...]}
    in_degree = build_in_degree(vertices, edges)  # {node: in_degree}

    # initialize queue with source nodes
    queue = deque([node for node in range(vertices) if in_degree[node] == 0])
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for child in graph[cur]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(order) != vertices:
        return []

    return order


def build_graph(num_vertices: int, edges: List[List[int]]) -> Dict[int, List[int]]:
    """Turns an edge list to an adjacency list"""
    graph = {i: [] for i in range(num_vertices)}
    for start, end in edges:
        graph[start].append(end)
    return graph


def build_in_degree(num_vertices: int, edges: List[List[int]]) -> Dict[int, int]:
    in_degree = {i: 0 for i in range(num_vertices)}
    for _, end in edges:
        in_degree[end] += 1
    return in_degree


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
