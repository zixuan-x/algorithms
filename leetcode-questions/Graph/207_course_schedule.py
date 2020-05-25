from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)  # {parent: [children]}
        # graph = {i: [] for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}
        sortedOrder = []
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            inDegree[child] += 1
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            course = sources.popleft()
            sortedOrder.append(course)
            for child in graph[course]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return len(sortedOrder) == numCourses

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
