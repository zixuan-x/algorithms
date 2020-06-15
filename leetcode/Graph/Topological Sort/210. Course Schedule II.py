from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                    
        return sortedOrder if len(sortedOrder) == numCourses else []

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