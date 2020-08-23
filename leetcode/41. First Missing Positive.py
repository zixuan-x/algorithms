class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
                # The following line does not work!!!
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
 
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
        