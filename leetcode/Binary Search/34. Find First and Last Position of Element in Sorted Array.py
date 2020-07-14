class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        return [self.findFirst(nums, target), self.findLast(nums, target)]
    
    def findFirst(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif target <= nums[mid]:
                right = mid 
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
    
    def findLast(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            elif target < nums[mid]:
                right = mid 
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1