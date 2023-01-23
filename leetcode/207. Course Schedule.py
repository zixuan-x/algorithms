from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        order_length = 0  # the max length of topological order we can get

        graph = self.build_graph(numCourses, prerequisites)
        in_degree = self.build_in_degree(numCourses, prerequisites)

        queue = deque([v for v in in_degree if in_degree[v] == 0])  # source nodes
        while queue:
            cur = queue.popleft()
            order_length += 1
            for child in graph[cur]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return order_length == numCourses

    def build_graph(self, num_vertices: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        graph = {v: [] for v in range(num_vertices)}
        for end, start in edges:
            graph[start].append(end)
        return graph

    def build_in_degree(self, num_vertices: int, edges: List[List[int]]) -> Dict[int, int]:
        in_degree = {v: 0 for v in range(num_vertices)}
        for end, _ in edges:
            in_degree[end] += 1
        return in_degree


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list: node -> [nodes]
        graph = self.buildGraph(numCourses, prerequisites)

        # 0: unvisited, 1: visiting, 2: visited
        visited = [0] * numCourses

        for i in range(numCourses):
            if self.dfs(graph, i, visited):
                return False

        return True

    def buildGraph(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
        return graph

    def dfs(self, graph, i, visited):
        if visited[i] == 1:
            return True
        elif visited[i] == 2:
            return False
        else:
            visited[i] = 1
            for neighbor in graph[i]:
                if self.dfs(graph, neighbor, visited):
                    return True

            visited[i] = 2
            return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}
        for c1, c2 in prerequisites:
            g[c2] = g.get(c2, []) + [c1]

        # 0 = unvisted, 1: visiting, 2: visited
        v = [0 for i in range(numCourses)]

        for i in range(numCourses):
            if self.dfs(i, v, g):
                return False

        return True

    def dfs(self, i, v, g):
        if v[i] == 1:
            return True
        elif v[i] == 2:
            return False

        v[i] = 1
        if i in g:
            for j in g[i]:
                if self.dfs(j, v, g):
                    return True
        v[i] = 2
        return False
