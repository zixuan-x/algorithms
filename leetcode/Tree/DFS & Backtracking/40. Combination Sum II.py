class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        combinations = []
        self.search(candidates, target, 0, [], combinations)
        return combinations
    
    def search(self, candidates, target, start, path, combinations):
        if start == len(candidates) or target <= 0:
            if target == 0:
                combinations.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.search(candidates, target - candidates[i], i + 1, path, combinations)
            path.pop()