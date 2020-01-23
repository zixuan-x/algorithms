class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        end = 0
        
        i = 1
        while i < len(nums):
            if nums[i] != nums[end]:
                end += 1
                nums[end] = nums[i]
            i += 1
                
        return end + 1