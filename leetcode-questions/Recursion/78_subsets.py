class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        cur = []
        self.combination(nums, cur, 0, results)
        return results
        
        
    def combination(self, nums, cur, index, results):
        # base cases
        if index == len(nums):
            results.append(list(cur))
            return
        
        # recursion rules
        self.combination(nums, cur, index + 1, results)
        
        cur.append(nums[index])
        self.combination(nums, cur, index + 1, results)
        cur.pop()

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def combination(nums, cur, index, results):
            if index == len(nums):
                results.append(list(cur))
                return
            else:
                combination(nums, cur, index + 1, results)
                
                cur.append(nums[index])
                combination(nums, cur, index + 1, results)
                cur.pop()
                
        results = []
        cur = []
        combination(nums, cur, 0, results)
        return results

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
        return subsets                
        