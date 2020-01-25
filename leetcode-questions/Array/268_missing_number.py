class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([x for x in range(len(nums) + 1)]) - sum(nums)