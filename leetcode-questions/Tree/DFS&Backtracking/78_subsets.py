class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, cur, res):
        if start >= len(nums):
            return
        else:
            for i in range(start, len(nums)):
                cur.append(nums[i])
                res.append(cur[:])
                self.dfs(nums, i + 1, cur, res)
                cur.pop()

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
        return subsets   

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], 0, res)
        return res
        
    def dfs(self, nums, cur, index, res):
        if index == len(nums):
            res.append(cur[:])
        else:
            self.dfs(nums, cur, index + 1, res)
            
            cur.append(nums[index])
            self.dfs(nums, cur, index + 1, res)
            cur.pop()

