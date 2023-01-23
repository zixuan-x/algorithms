"""
Union-Find
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        ranks = [1 for i in range(n + 1)]
        
        for u, v in edges:
            if self.find(u, parents) == self.find(v, parents):
                return [u, v]
            self.union(u, v, parents, ranks)
        return []
            
    def find(self, u, parents):
        if u != parents[u]:
            parents[u] = self.find(parents[u], parents)
        return parents[u]
    
    def union(self, u, v, parents, ranks):
        pu, pv = self.find(u, parents), self.find(v, parents)
        if pu == pv: return False
        if ranks[pu] < ranks[pv]:
            parents[pu] = pv
        elif ranks[pu] > ranks[pv]:
            parents[pv] = pu
        else:
            parents[pu] = pv
            ranks[pv] += 1
        return True

"""
DFS
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = {} # node -> [node]
        for u, v in edges:
            visited = set()
            if self.hasPath(u, v, visited, g):
                return [u, v]
            g[u] = g.get(u, []) + [v]
            g[v] = g.get(v, []) + [u]
        return []
        
    def hasPath(self, cur, target, visited, g) -> bool:
        if cur == target:
            return True
        elif cur not in g or target not in g:
            return False
        else:
            visited.add(cur)
            for neighbor in g[cur]:
                if neighbor not in visited and self.hasPath(neighbor, target, visited, g):
                    return True
            return False
            
            