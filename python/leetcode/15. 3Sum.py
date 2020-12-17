'''
1. Sort
2. nums[i] == nums[i - 1]
3. nums[i] > 0
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] > 0: break
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return results