class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(1, 0, [], n, k, res)
        return res
        
    def dfs(self, num, count, cur, n, k, res):
        """
        1. every level represents a number in 1..n
        2. there are n levels
        3. branches are 0 or 1
        """
        if num > n or count >= k:
            if count == k:
                res.append(cur[:])
        else:
            # choose
            cur.append(num)
            self.dfs(num + 1, count + 1, cur, n, k, res)
            cur.pop()
            
            # not choose
            self.dfs(num + 1, count, cur, n, k, res)