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
            