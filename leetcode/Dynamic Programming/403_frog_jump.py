class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        
        d = {stone: set() for stone in stones}
        d[1].add(1)
        for i in range(1, len(stones) - 1):
            for unit in d[stones[i]]:
                for step in [unit - 1, unit, unit + 1]:
                    if stones[i] + step in d and step != 0:
                        d[stones[i] + step].add(step)
        
        return len(d[stones[-1]]) > 0

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        return self.dfs(0, 1, stones[-1], set(), set(stones))
        
    def dfs(self, pos, speed, target, visited, stones):
        if (pos, speed) in visited or pos not in stones:
            return False
        elif pos == target:
            return True
        else:
            visited.add((pos, speed))
            speeds = [speed - 1, speed, speed + 1] if pos != 0 else [1]
            for s in speeds:
                if self.dfs(pos + s, s, target, visited, stones):
                    return True
            return False