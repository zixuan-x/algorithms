class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = {}
        for fromNode, toNode in edges:
            g[fromNode] = g.get(fromNode, []) + [toNode]
            g[toNode] = g.get(toNode, []) + [fromNode]
        visited = [False] * (n + 1)
        visited[1] = True
        return self.dfs(g, 1, visited, t, target)
        
    def dfs(self, g, cur, visited, secondsLeft, target):
        if secondsLeft == 0:
            return 1 if cur == target else 0
        else:
            chances = 0
            options = 0
            if cur in g:
                for neighbor in g[cur]:
                    if not visited[neighbor]:
                        options += 1
                        visited[neighbor] = True
                        chances += self.dfs(g, neighbor, visited, secondsLeft - 1, target)
            return chances / options if options else (1 if cur == target else 0)