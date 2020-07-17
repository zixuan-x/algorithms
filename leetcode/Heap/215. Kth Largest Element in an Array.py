from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = list(map(lambda x: -x, nums))
        heapify(maxHeap)
        res = 0
        for i in range(k):
            res = heappop(maxHeap)
        return -res

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = 0
        for i in range(len(nums) - k + 1):
            res = heappop(nums)
        return res
