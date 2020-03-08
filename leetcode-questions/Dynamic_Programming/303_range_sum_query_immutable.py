class NumArray:
    """
    [3:17] start
    一边上课一边刷题hhh
    dp(i) -> sum(nums[:i + 1])
    [3:21] solved
    """

    def __init__(self, nums: List[int]):
        self.dp = [0] * len(nums)
        for i in range(len(nums)):
            self.dp[i] = self.dp[i - 1] + nums[i] if i > 0 else nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i - 1] if i > 0 else self.dp[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)