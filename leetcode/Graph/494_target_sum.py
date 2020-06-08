class Solution:
    """
    1. every level represent an index in nums
    2. there are len(nums) levels
    3. there are two branches at every level
    
    DFS Parameters: nums, index, curSum, S, res
    
    1. we go from sum 0
    2. go to two branches, + or -
    3. update curSum
    4. if we are at the last level, check if curSum == S
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        res = [0]
        self.dfs(nums, 0, 0, S, res)
        return res[0]
        
    def dfs(self, nums, index, curSum, S, res):
        if index == len(nums):
            res[0] += 1 if curSum == S else 0
        else:
            # +
            self.dfs(nums, index + 1, curSum + nums[index], S, res)
            
            # - 
            self.dfs(nums, index + 1, curSum - nums[index], S, res)

class Solution:
    """
    1. dp(i, j) -> ways to sum to j using nums[:i + 1]
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        numsSum = sum(nums)
        offset = numsSum
        if numsSum < S: return 0
        ways = [[0] * (numsSum + offset + 1) for _ in range(n + 1)]
        ways[0][offset] = 1
        for i in range(n):
            for j in range(nums[i], 2 * numsSum + 1 - nums[i]):
                if ways[i][j]:
                    ways[i + 1][j + nums[i]] += ways[i][j]
                    ways[i + 1][j - nums[i]] += ways[i][j]
        
        return ways[-1][S + offset]