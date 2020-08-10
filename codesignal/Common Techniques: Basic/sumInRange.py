def sumInRange(nums, queries):
    n = len(nums)
    prefixSum = [0] * (n + 1)  # suffixSum, postfixSum
    for i in range(n):
        prefixSum[i] += nums[i] + prefixSum[i - 1]
    
    result = 0
    for start, end in queries:
        result += prefixSum[end] - prefixSum[start - 1]
    return result % ((10 ** 9) + 7)