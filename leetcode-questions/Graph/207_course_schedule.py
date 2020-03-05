class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}
        for c1, c2 in prerequisites:
            g[c2] = g.get(c2, []) + [c1]
            
        # 0 = unvisted, 1: visiting, 2: visited
        v = [0 for i in range(numCourses)]
        
        for i in range(numCourses):
            if self.dfs(i, v, g):
                return False
        
        return True
    
    def dfs(self, i, v, g):
        if v[i] == 1:
            return True
        elif v[i] == 2:
            return False
        
        v[i] = 1
        if i in g:
            for j in g[i]:
                if self.dfs(j, v, g):
                    return True
        v[i] = 2
        return False
