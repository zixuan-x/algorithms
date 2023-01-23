class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([x for x in range(len(nums) + 1)]) - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))