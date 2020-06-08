class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, 0, [], 0, target, res)
        return res
    
    def dfs(self, candidates, curSum, curList, start, target, res):
        if start >= len(candidates) or curSum >= target:
            if curSum == target:
                res.append(curList[:])
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curList.append(candidates[i])
                self.dfs(candidates, curSum + candidates[i], curList, i + 1, target, res)
                curList.pop()