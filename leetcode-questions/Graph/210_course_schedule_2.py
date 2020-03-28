class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sortedOrder = []
        
        # adjacency list
        graph, inDegree = self.buildGraph(numCourses, prerequisites)
        
        # sources
        sources = deque()
        for key, value in inDegree.items():
            if value == 0:
                sources.append(key)
        
        # BFS
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != numCourses:
            return []
        return sortedOrder
        
    
    def buildGraph(self, numCourses, prerequisites):
        graph = defaultdict(list)
        inDegree = {i: 0 for i in range(numCourses)}
        
        for u, v in prerequisites:
            graph[v].append(u)
            inDegree[u] += 1
        
        return graph, inDegree

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        g = {}
        for c1, c2 in prerequisites:
            g[c2] = g.get(c2, []) + [c1]
        v = [0 for i in range(numCourses)]
        
        for i in range(numCourses):
            if not v[i]:
                if self.dfs(i, g, v, order):
                    return []
        
        return reversed(order)
    
    def dfs(self, i, g, v, order):
        if v[i] == 1:
            return True
        elif v[i] == 2:
            return False
        
        v[i] = 1
        if i in g:
            for j in g[i]:
                if self.dfs(j, g, v, order):
                    return True
        order.append(i)
        v[i] = 2
        return False