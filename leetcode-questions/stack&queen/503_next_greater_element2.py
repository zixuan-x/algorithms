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