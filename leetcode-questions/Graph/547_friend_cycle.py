class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parents = [i for i in range(n)]
        ranks = [1 for _ in range(n)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if ranks[px] < ranks[py]:
                parents[px] = py
            elif ranks[px] > ranks[py]:
                parents[py] = px
            else:
                parents[px] = py
                ranks[py] += 1
        
        # iterate through all nodes and union friends
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    union(i, j)
                
        # find out how many roots there are
        count = 0
        for i in range(n):
            if parents[i] == i:
                count += 1
        return count

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i, M, visited)
                count += 1
        return count
        
        
    def dfs(self, i, M, visited):
        visited[i] = 1
        for j in range(len(M[i])):
            if M[i][j] and not visited[j]:
                self.dfs(j, M, visited)