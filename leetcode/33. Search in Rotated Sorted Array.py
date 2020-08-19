'''
if nums[left] <= target < nums[mid]: 这里要有等号，因为 target can be equal to nums[left]
'''
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


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]: # [left: mid] increasing
                if nums[left] <= target < nums[mid]: # target can be equal to nums[left]
                    right = mid
                else:
                    left = mid
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                return mid
            
        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1
                