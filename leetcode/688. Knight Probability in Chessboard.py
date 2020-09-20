from collections import deque

'''
dp - memo search:
'''
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # memo = [[[0] * N for _ in range(N)] for _ in range(N)]
        return self.search(N, K, r, c, {})
    
    def search(self, N, K, r, c, memo):
        if r < 0 or r >= N or c < 0 or c >= N:
            return 0
        if K == 0:
            return 1
        if (r, c, K) in memo:
            return memo[(r, c, K)]
        
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        rate = 0
        for dr, dc in directions:
            rate += 0.125 * self.search(N, K - 1, r + dr, c + dc, memo)
        
        memo[(r, c, K)] = rate
        return rate
        
        

'''
TLE:
'''
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        remains = 0
        queue = deque([(r, c, 1, 0)])
        while queue:
            r, c, rate, moves = queue.popleft()
            if moves == K:
                remains += rate
                continue
            for dr, dc in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                queue.append((nr, nc, rate / 8, moves + 1))
        return remains