class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and memo[j] + 1 > memo[i]:
                    memo[i] = memo[j] + 1
        return max(memo, default=0)
        