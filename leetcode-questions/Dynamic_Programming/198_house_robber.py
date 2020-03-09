class Solution:
    """
    [3:01] start
    dp(i) -> max (rob or not)
    Two states for one house.
    The result of one house only depend on the prev house.
    --- just like paint house
    
    rob = norob + nums[i]
    norob = max(rob, norob)
    [3:15] soolved
    """
    def rob(self, nums: List[int]) -> int:
        rob, norob = 0, 0
        for i in range(len(nums)):
            rob, norob = nums[i] + norob, max(rob, norob)
        return max(rob, norob)
            
        