''' 1.  '''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.search(nums, 0, [], results)
        return results
        
        
    def search(self, nums, start, path, results):
        results.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.search(nums, i + 1, path, results)
            path.pop()

''' 2.  '''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
        return subsets   

''' 3.  '''
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

