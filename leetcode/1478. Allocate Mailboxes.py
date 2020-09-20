class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])
        return self.memoSearch(houses, 0, k, {}, costs)
        
    def memoSearch(self, houses, i, k, memo, costs):
        n = len(houses)
        if i == n and k == 0:
            return 0
        if k == 0 or i == n:
            return float('inf')
        if (k, i) in memo:
            return memo[(k, i)]
        
        distance = float('inf')
        for j in range(i, n):
            distance = min(distance, costs[i][j] + self.memoSearch(houses, j + 1, k - 1, memo, costs))
        memo[(k, i)] = distance
        return distance