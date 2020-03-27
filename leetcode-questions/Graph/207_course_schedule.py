from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedOrder = []
        
        # adjacency list
        graph, inDegree = self.buildGraph(numCourses, prerequisites)
        
        sources = deque()
        for key, value in inDegree.items():
            if value == 0:
                sources.append(key)
 
        
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
                    
        return len(sortedOrder) == numCourses
        
        
    def buildGraph(self, numCourses, prerequisites):
        graph = defaultdict(list)
        inDegree = {i: 0 for i in range(numCourses)}
        
        for u, v in prerequisites:
            graph[v].append(u)
            inDegree[u] += 1
        
        return graph, inDegree
   

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
