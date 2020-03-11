class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # define find
        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]
                
        # initialize parents, roots, sizes, edge1, edge2
        n = len(edges)
        # n - 1 edges, n nodes, index start from 0 -> size = n + 1
        parents = [0] * (n + 1)
        roots = [0] * (n + 1)
        sizes = [1] * (n + 1)
        # edge1 ,2?
        edge1 = []
        edge2 = []
        
        # initialize parents to see if there is two indegree nodes
        for i in range(n):
            u, v = edges[i][0], edges[i][1]
            if parents[v] > 0:
                edge1 = [parents[v], v]
                edge2 = [u, v]
                edges[i][0], edges[i][1] = -1, -1 # delete edge
            parents[v] = u
        
        # union-find
        for u, v in edges:
            # skip deleted edge
            if u < 0 or v < 0: continue
            if not roots[u]: roots[u] = u
            if not roots[v]: roots[v] = v
            ru, rv = find(u), find(v)
            
            if ru == rv: # if cycle
                return edge1 if edge1 else [u, v]
                
            if sizes[ru] > sizes[rv]:
                ru, rv = rv, ru
            roots[ru] = rv
            sizes[rv] += sizes[ru]
            
        return edge2
            