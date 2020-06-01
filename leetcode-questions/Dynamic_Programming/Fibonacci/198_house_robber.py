class Solution:
    """
    [3:01] start
    dp(i) -> max (rob or not)
    Two states for one house.
    The result of one house only depend on the prev house.
    --- just like paint house
    
    rob = norob + nums[i]
    norob = max(rob, norob)
    [3:15] solved
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        states = [[-1] * 2 for _ in range(n)]
        states[0][0] = nums[0]
        states[0][1] = 0
        
        def helper(n):
            if states[n][0] < 0:
                rob, norob = helper(n - 1)
                states[n][0] = norob + nums[n]
                states[n][1] = max(rob, norob)
            return (states[n][0], states[n][1])
        
        return max(helper(n - 1))
            
class Solution:
    '''
    dp(i) = 抢到第i个房子时，抢或不抢第i个房子的最大收益
        dp(i)[0] = 不抢
        dp(i)[1] = 抢
        
    dp(i)[0] = max(dp(i - 1)[0], dp(i - 1)[1])
    dp(i)[1] = dp(i - 1)[0] + money[i]
    
    dp(0)[0] = 0
    dp(0)[1] = 1
    '''
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        rob, norob = nums[0], 0
        for i in range(1, len(nums)):
            rob, norob = norob + nums[i], max(rob, norob)
        return max(rob, norob)
        