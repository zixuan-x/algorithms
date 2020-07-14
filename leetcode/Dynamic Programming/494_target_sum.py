class Solution:
    """
    1. dp(i, j) -> ways to sum to j using nums[:i + 1]
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        numsSum = sum(nums)
        offset = numsSum
        if numsSum < S: return 0
        ways = [[0] * (numsSum + offset + 1) for _ in range(n + 1)]
        ways[0][offset] = 1
        for i in range(n):
            for j in range(nums[i], 2 * numsSum + 1 - nums[i]):
                if ways[i][j]:
                    ways[i + 1][j + nums[i]] += ways[i][j]
                    ways[i + 1][j - nums[i]] += ways[i][j]
        
        return ways[-1][S + offset]