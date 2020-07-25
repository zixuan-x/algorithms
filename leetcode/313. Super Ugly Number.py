'''
1. 
Time Complexity: O(nk)
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = [1] * n
        idx = [0] * len(primes)
        for i in range(1, n):
            nums[i] = float('inf')
            for j in range(len(primes)):
                nums[i] = min(nums[i], primes[j] * nums[idx[j]])
            for j in range(len(primes)):
                while primes[j] * nums[idx[j]] <= nums[i]:
                    idx[j] += 1
        return nums[-1]

'''
2. Heap
Time Complexity: O(nklogn)
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        minHeap = [1]
        visited = set([1])
        for _ in range(n):
            num = heappop(minHeap)
            for factor in primes:
                if factor * num not in visited:
                    visited.add(factor * num)
                    heappush(minHeap, factor * num)
        return num