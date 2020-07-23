'''
Time Complexity: O(nlogk)
'''
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxHeap = []  # [(-distance ** 2, x, y)]
        for x, y in points:
            heappush(maxHeap, (-(x ** 2 + y ** 2), x, y))
            if len(maxHeap) > K:
                heappop(maxHeap)
        return [[x, y] for _, x, y in maxHeap]
        
'''
Time Complexity: O(nlogn)
'''
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        minHeap = []  # [(distance ** 2, x, y)]
        for x, y in points:
            heappush(minHeap, (x ** 2 + y ** 2, x, y))
            
        results = []
        for i in range(K):
            _, x, y = heappop(minHeap)
            results.append([x, y])
        return results