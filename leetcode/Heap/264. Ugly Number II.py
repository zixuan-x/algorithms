'''
1. 
Time Complexity: O(4n) = O(n)
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1] * n
        idx2, idx3, idx5 = 0, 0, 0
        for i in range(1, n):
            nums[i] = min(2 * nums[idx2], 3 * nums[idx3], 5 * nums[idx5])
            if nums[i] == nums[idx2] * 2:
                idx2 += 1
            if nums[i] == nums[idx3] * 3:
                idx3 += 1
            if nums[i] == nums[idx5] * 5:
                idx5 += 1
        return nums[n - 1]

'''
2. 
Time Complexity: O(nlogn)
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        visited = set([1])
        for _ in range(n):
            num = heappop(minHeap)
            for factor in [2, 3, 5]:
                if num * factor not in visited:
                    heappush(minHeap, num * factor)
                    visited.add(num * factor)
        return num
