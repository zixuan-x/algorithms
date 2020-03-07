class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, start, cur, res):
        if start >= len(nums):
            return
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                res.append(cur[:])
                self.dfs(nums, i + 1, cur, res)
                cur.pop()
                