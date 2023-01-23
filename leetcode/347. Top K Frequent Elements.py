'''
1. 
Time Complexity: O(n)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequencies = defaultdict(list)
        for key, value in counter.items():
            frequencies[value].append(key)
        results = []
        for i in range(len(nums), -1, -1):
            if len(results) == k: break
            results += frequencies[i]
        return results


'''
2. 
Time Complexity: O(nlogk)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        minHeap = []
        for key, value in counter.items():
            heappush(minHeap, (value, key))
            if len(minHeap) > k:
                heappop(minHeap)
        return [key for _, key in minHeap]