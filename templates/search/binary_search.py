from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """Assuming nums is sorted in ascending order"""
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid

    # post-processing
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1
