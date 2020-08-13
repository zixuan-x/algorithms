class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        permutations = []
        used = [False] * len(nums)
        self.search(nums, used, [], permutations)
        return permutations
    
    def search(self, nums, used, path, permutations):
        if len(path) == len(nums):
            permutations.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(nums[i])
            self.search(nums, used, path, permutations)
            path.pop()
            used[i] = False