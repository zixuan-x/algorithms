from typing import List

def sum(nums: List[int]) -> int:
    # return sum(nums)
    sum = 0
    for num in nums:
        sum += num
    return sum

list = [1,2,3,4]

print(sum(list))