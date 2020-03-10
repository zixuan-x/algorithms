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
                