class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        combinations = []
        self.search(candidates, target, 0, [], combinations)
        return combinations
        
    def search(self, candidates, target, start, path, combinations):
        if start == len(candidates) or target <= 0:
            if target == 0:
                combinations.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.search(candidates, target - candidates[i], i, path, combinations)
            path.pop()


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        combinations = []
        self.dfs(candidates, 0, [], target, combinations)
        return combinations
        
    def dfs(self, candidates, index, path, target, combinations):
        if index == len(candidates) or target <= 0:
            if target == 0:
                combinations.append(path[:])
            return
        
        for i in range(target // candidates[index] + 1):
            path += [candidates[index]] * i
            self.dfs(candidates, index + 1, path, target - candidates[index] * i, combinations)
            for j in range(i):
                path.pop()