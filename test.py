# mission = [0, 0, 3, 2, 4, 1]
mission = [0, 0, -1, -2, 3, -5]
'''
dp state: dp[i] = max score after Mario jumped to ith position
state transfer: dp[i] = max(dp[i], dp[j] + mission[i] * mission[j] * ((i - j) ** 2))
base case: dp[0] = 0
'''
def Mario(mission):
    # handling edge case
    if not mission:
        return 0
    
    # initialize a dp array with intial value of 0
    dp = [0] * len(mission)

    for i in range(len(mission)):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + mission[i] * mission[j] * ((i - j) ** 2))
    
    return max(dp)

print(Mario(mission))