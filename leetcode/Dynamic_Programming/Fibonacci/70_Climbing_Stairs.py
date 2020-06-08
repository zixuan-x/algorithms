# recursion
# Top down - TLE
def climbStairs1(self, n):
    if n <= 2: return n
    return self.climbStairs(n-1) + self.climbStairs(n-2)

# memoization (top down)
def climbStairs(self, n: int) -> int:
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    return self.climb(n, dp)
        
def climb(self, i, dp):
		if dp[i] == 0:
		    dp[i] = self.climb(i - 1, dp) + self.climb(i - 2, dp)
		return dp[i]

# dynamic programming (bottom up) - O(n) space
def climbStairs(self, n: int) -> int:
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]

# dynamic programming (bottom up) - O(1) space
def climbStairs(self, n: int) -> int:
    if n <= 2: return n
    a, b = 1, 2
    res = 0
    for i in range(3, n + 1):
        temp = b
        b = a + b
        a = temp
    return b