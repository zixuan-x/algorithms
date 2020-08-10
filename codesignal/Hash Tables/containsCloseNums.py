from collections import defaultdict

def containsCloseNums(nums, k):
    positions = defaultdict(list)
    for i in range(len(nums)):
        num = nums[i]
        if num in positions:
            for position in positions[num]:
                if abs(position - i) <= k:
                    return True
                    
        positions[num].append(i)    
    return False
