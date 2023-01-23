class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        offset = k % len(nums)
        
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, offset - 1)
        reverse(nums, offset, len(nums) - 1)
        
        