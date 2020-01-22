from typing import List

def minimum(nums: List[int]) -> int:
    res = nums[0]
    for num in nums[1:]:
        if num < res:
            res = num
    return res

list = [5,1,2,3]
print(minimum(list))

def second_minimum1(nums: List[int]) -> int:
    first = min(nums)
    second = None
    for num in nums:
        if num == first:
            continue
        elif second == None:
            second = num
        elif num < second:
            second = num
    return second

print(second_minimum1(list))

def second_minimum2(nums: List[int]) -> int:
    if len(nums) < 2:
        raise RuntimeError

    first, second = min(nums), max(nums)
    for num in nums:
        

    
