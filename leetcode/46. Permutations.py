class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.search(nums, 0, permutations)
        return permutations
    
    def search(self, nums, start, permutations):
        if start == len(nums) - 1: # if all previous elements are determiend, then the last one is determined
            permutations.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.search(nums, start + 1, permutations)
            nums[start], nums[i] = nums[i], nums[start]

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        results = []

        # 如果数组为空直接返回空
        if nums is None:
            return []

        # dfs
        used = [0] * len(nums)
        self.dfs(nums, used, [], results)
        return results

    def dfs(self, nums, used, current, results):

        # 找到一组排列，已到达边界条件
        if len(nums) == len(current):
            # 因为地址传递，在最终回溯后current为空导致results中均为空列表
            # 所以不能写成results.append(current)
            results.append(current[:])
            return

        for i in range(len(nums)):
            # i位置这个元素已经被用过
            if used[i]:
                continue

            # 继续递归
            current.append(nums[i])
            used[i] = 1
            self.dfs(nums, used, current, results)
            used[i] = 0
            current.pop()
