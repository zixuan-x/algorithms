class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            res.append(-1)
            for j in range(1, n):
                index = (i + j) % n
                if nums[index] > nums[i]:
                    res[i] = nums[index]
                    break
        return res

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n * 2 - 1):
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]
            
            if i < n:
                stack.append(i)
        return res