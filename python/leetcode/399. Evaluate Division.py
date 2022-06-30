from collections import defaultdict, deque

'''
union/find:
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(x): # X / root = res
            if parents[x][0] != x:
                rx, vx = find(parents[x][0])
                parents[x] = (rx, vx * parents[x][1])
            return parents[x]
        
        # def union(x, y):
        def divide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry:
                return -1.0
            return vx / vy
        
        parents = {} # A -> B, cost = A / B
        
        # iterate through equations to union nodes
        for (x, y), v in zip(equations, values):
            if x not in parents and y not in parents:
                parents[x] = (y, v)
                parents[y] = (y, 1.0)
            elif x not in parents:
                parents[x] = (y, v)
            elif y not in parents:
                parents[y] = (x, 1.0 / v)
            else:
                rx, vx = find(x) # x / root1 = vx
                ry, vy = find(y) # y / root2 = vy
                                 # x / y = v
                # want: root1 / root2 = ?
                parents[rx] = (ry, v * vy / vx) # v * vy / vx = (x / root2) * (root1 / x)
            
        # iterate queries to get resultls
        return [divide(x, y) if x in parents and y in parents else -1.0 for x, y in queries]
        
'''
search:
m -> queries, q -> equations(# of Edges), n -> # of nodes
q -> 0 ~ n^2
time: O(m * (q + n))  -> O(m * n ^ 2)

time complexity to visited a graph: O(V + E)
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)  # {node1: [(node2, conversion)]}
        # path compression -> { node : { node : weight } }
        for i in range(len(equations)):
            node1, node2 = equations[i]
            conversion = values[i]
            graph[node1].append((node2, conversion))
            graph[node2].append((node1, 1 / conversion))
            
        result = []
        for start, end in queries:
            if start not in graph or end not in graph:
                result.append(-1.0)
            else:
                result.append(self.search(graph, start, end))
        return result
    
    def search(self, graph, start, end):
        if start == end:
            return 1.0
        visited = set([start])
        queue = deque([(start, 1.0)])
        while queue:
            node, conversion = queue.popleft()
            if node == end:
                return conversion
            for neighbor, rate in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, conversion * rate))
        return -1.0
