class Solution:
    """
    dp(i) -> max sum from nums[0:i + 1], including the last element
    dp(i + 1) = dp(i) + nums[i] if dp(i) > 0 else nums[i]
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums)
        maxSum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] if dp[i - 1] < 0 else dp[i - 1] + nums[i]
            maxSum = max(maxSum, dp[i])
        return maxSum