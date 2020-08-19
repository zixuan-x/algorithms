def findEvenDigits(nums):
    result = 0
    for num in nums:
        result += len(str(num)) % 2 == 0
    return result

print(findEvenDigits([12, 3, 5, 3456]) == 2)