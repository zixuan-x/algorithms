'''
sliding window
time: O(n)
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = float('inf')
        left, windowSum = 0, 0
        for right in range(len(nums)):
            windowSum += nums[right]
            while windowSum >= s:
                length = min(length, right - left + 1)
                windowSum -= nums[left]
                left += 1
        return length if length != float('inf') else 0