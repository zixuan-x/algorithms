class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[2]
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                
                temp = nums[i] + nums[left] + nums[right]
                
                if temp == target:
                    return target
                
                if abs(temp - target) < abs(result - target):
                    result = temp
                
                if temp > target:
                    right -= 1
                else:
                    left += 1
                
        return result
            
        