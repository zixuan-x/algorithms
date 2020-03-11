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
        

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # construct graph
        g = {} #{ node : { node : weight } }
        # g[A][B] 
        for i in range(len(equations)):
            A, B = equations[i]
            g[A] = g.get(A, []) + [(B, values[i])]
            g[B] = g.get(B, []) + [(A, 1 / values[i])]
        

        res = []
        # bfs
        for i in range(len(queries)):
            S, T = queries[i]
            if S not in g or T not in g:
                res.append(-1.0)
                continue
            res.append(self.bfs(S, T, g))# FIXME
        return res
        
        
    def bfs(self, S, T, g):
        if S == T:
            return 1.0
        queue = collections.deque([(S, 1)])
        visited = set([S])
        while queue:
            cur, product = queue.popleft()
            for neighbor, rate in g[cur]:
                if neighbor == T: return product * rate
                if neighbor not in visited:
                    queue.append((neighbor, product * rate))
        return -1.0
                