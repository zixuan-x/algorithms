class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        result = nums[0]
        maxEnd, minEnd = result, result
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxEnd, minEnd = minEnd, maxEnd
            
            maxEnd = max(nums[i], maxEnd * nums[i])
            minEnd = min(nums[i], minEnd * nums[i])
            
            result = max(result, maxEnd)
            
        return result