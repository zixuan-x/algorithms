def findLongestSubarrayBySum(s, arr):
    result = [-1, -1]
    windowSum = 0
    left = 0
    for right in range(len(arr)):
        windowSum += arr[right]
        while windowSum > s:
            windowSum -= arr[left]
            left += 1
        if windowSum == s:
            if result == [-1, -1]:
                result = [left, right]
            elif (right - left + 1) > (result[1] - result[0] + 1):
                result = [left, right]
            elif (right - left + 1) == (result[1] - result[0] + 1) and left < result[0]:
                result = [left, right]
                
    if result == [-1, -1]:
        return [-1]
    else:
        return [result[0] + 1, result[1] + 1]