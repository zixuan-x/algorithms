'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28218/My-8ms-C%2B%2B-solution-(o(logn)-on-average-o(n)-worst-case)
The only difference is that due to the existence of duplicates, we can have nums[left] == nums[mid] 
and in that case, the first half could be out of order (i.e. NOT in the ascending order, 
e.g. [3 1 2 3 3 3 3]) and we have to deal this case separately. In that case, it is guaranteed 
that nums[right] also equals to nums[mid], so what we can do is to check 
if nums[mid]== nums[left] == nums[right] before the original logic, and if so, we can move left 
and right both towards the middle by 1. and repeat.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
        return nums[left] == target or nums[right] == target