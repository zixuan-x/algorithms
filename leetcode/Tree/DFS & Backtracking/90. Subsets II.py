class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.search(nums, 0, [], subsets)
        return subsets
    
    def search(self, nums, start, path, subsets):
        subsets.append(path[:])
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.search(nums, i + 1, path, subsets)
            path.pop()
        
    