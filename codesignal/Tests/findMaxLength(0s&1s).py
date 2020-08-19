def findMaxLength(nums: List[int]) -> int:
    if not nums:
        return 0
    
    count = 0
    maxLength = 0
    table = {0: -1}
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        
        if count in table:
            maxLength = max(maxLength, i - table[count])
        else:
            table[count] = i
    return maxLength