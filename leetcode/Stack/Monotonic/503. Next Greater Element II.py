'''backward'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in reversed(range(2 * n)):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            res[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        return res