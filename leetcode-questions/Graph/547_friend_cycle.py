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