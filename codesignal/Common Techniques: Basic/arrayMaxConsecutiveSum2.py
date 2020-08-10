def arrayMaxConsecutiveSum2(inputArray):
    if not inputArray:
        return 0
    result = float('-inf')
    curSum = 0
    for num in inputArray:
        curSum += num
        if num > curSum:
            curSum = num
        result = max(result, curSum)
    return result
        


def arrayMaxConsecutiveSum2(inputArray):
    maxsum = inputArray[0]
    l = len(inputArray)
    cumsum = inputArray[0]
    for i in range(1, l):
        cumsum += inputArray[i]
        if inputArray[i] > cumsum:
            cumsum = inputArray[i]
        maxsum = max(maxsum, cumsum)
    return maxsum
    
