'''backward'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i in reversed(range(len(T))):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res