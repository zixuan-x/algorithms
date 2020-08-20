'''
heap? quick select?
'''
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        minCost = 0
        costs.sort(key=lambda cost: cost[1] - cost[0])
        for i in range(n):
            minCost += costs[i][1] + costs[n + i][0]
        return minCost
        

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        minCost = 0
        refund = []
        for A, B in costs:
            refund.append(B - A)
            minCost += A
        refund.sort()
        for i in range(n):
            minCost += refund[i]
        return minCost
        
        