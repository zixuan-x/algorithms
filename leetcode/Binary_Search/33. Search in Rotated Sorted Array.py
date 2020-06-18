class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target == nums[mid]:  # found target
                return mid
            elif nums[mid] > nums[left]:  # [:mid] in acsending order
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:  # [mid:] in acsending order
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1