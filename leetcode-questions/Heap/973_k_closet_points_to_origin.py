class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # (distance, (x, y))
        heap = []
        
        for x, y in points:
            heapq.heappush(heap, (- (x ** 2 + y ** 2), (x, y)))
            if len(heap) > K:
                heapq.heappop(heap)
                
        return [[x, y] for _, (x, y) in heap]
        