class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(self.robHelper(nums, 0, len(nums) - 2), self.robHelper(nums, 1, len(nums) - 1))
        
    def robHelper(self, nums, left, right):
        rob, norob = 0, 0
        for i in range(left, right + 1):
            rob, norob = nums[i] + norob, max(rob, norob)
        return max(rob, norob)
            
        