from collections import Counter

def findMostCommon(nums):
    c = Counter(nums)
    maxFreq = max(c.values())
    result = []
    for k in c:
        if c[k] == maxFreq:
            result.append(k)
    return result

print(findMostCommon([2, 2, 3, 3, 5]) == [2, 3])