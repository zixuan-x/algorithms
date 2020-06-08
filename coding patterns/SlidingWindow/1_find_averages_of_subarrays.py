def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K - 1:
            result.append(windowSum / K)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result
