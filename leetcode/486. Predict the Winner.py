'''
1. min/max
time complexity: O(2 ^ n)
space complexity: O(n) for stack
'''
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.getScore(nums, 0, len(nums) - 1)
        
    def getScore(self, nums, l, r):
        '''
        Max diff (my_score - op_score) of subarray nums[l] ~ nums[r].
        '''
        if l == r:
            return nums[l]
        return max(nums[l] - self.getScore(nums, l + 1, r), nums[r] - self.getScore(nums, l, r - 1))
        
'''
2. memo
time complexity: O(n ^ 2)
space complexity: O(n ^ 2 + n for stack)
'''
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.getScore(nums, 0, len(nums) - 1, {}) >= 0
        
    def getScore(self, nums, l, r, memo):
        '''
        Max diff (my_score - op_score) of subarray nums[l] ~ nums[r].
        '''
        if l == r:
            return nums[l]
        
        if (l, r) not in memo:
            memo[(l, r)] = max(nums[l] - self.getScore(nums, l + 1, r, memo), nums[r] - self.getScore(nums, l, r - 1, memo))
        return memo[(l, r)]