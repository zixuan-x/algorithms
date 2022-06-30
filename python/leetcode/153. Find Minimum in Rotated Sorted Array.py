class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return -1
        if nums[0] < nums[-1]: return nums[0]
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:  # [:mid] in acsending order
                left = mid
            else:  # [mid:] in acsending order
                right = mid
        return min(nums[left], nums[right])