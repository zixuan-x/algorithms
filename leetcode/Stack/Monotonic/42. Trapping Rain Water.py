''' 1. Brute Force - O(n ^ 2) time, O(1) space '''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        n = len(height)
        res = 0

        for i in range(n):
            left_max, right_max = 0, 0

            # find max in [:i]

            # find max in [i:]

            res += min(left_max, right_max) - height[i]

        return res

''' 
2. DP - 3 pass - O(n) time, O(n) space 
核心思路：不要想整体，而应该去想局部
“具体来说，仅仅对于位置 i，能装下多少水呢？”
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        n = len(height)
        
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        right_max[-1] = height[-1]
        
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
        
        for i in reversed(range(n - 1)):
            right_max[i] = max(height[i], right_max[i + 1])
        
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
            
        return res

''' 3. Two Pointers - '''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[0], height[n - 1]
        res = 0
        
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
                
        return res