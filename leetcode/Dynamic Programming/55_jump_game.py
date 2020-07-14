class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        i = 0
        upper = 0
        while i < n and upper >= i:
            upper = max(upper, i + nums[i])
            i += 1
        
        return upper >= n - 1

class Solution:
    '''
    Most DP problems just start with brute force search (DFS)
    '''
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[False, False] for _ in range(n)]
        dp[-1][0], dp[-1][1] = True, True
        return self.jump(nums, dp, 0)
    
    def jump(self, nums, dp, i):
        if not dp[i][1]:
            for step in range(1, nums[i] + 1):
                if i + step < len(nums) and self.jump(nums, dp, i + step):
                    dp[i][0] = True
                    break
            dp[i][1] = True
        return dp[i][0]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for step in range(1, nums[i] + 1):
                if i + step >= len(nums): break
                if i + step < len(nums) and dp[i + step]:
                    dp[i] = True
                    break
        return dp[0]