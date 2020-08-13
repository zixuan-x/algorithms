class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first turning point
        i = len(nums) - 1
        while i > 0:            
            if nums[i - 1] < nums[i]:
                break
            i -= 1
            
        # if in descending order, return reversed order
        if i == 0:
            nums.reverse()
            return nums
        
        # reverse nums[i:]
        left, right = i, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        # swap nums[i - 1] with the first elemenet larger than it after reverse
        j = i - 1
        while i < len(nums):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
            i += 1
        return nums
        
        
        