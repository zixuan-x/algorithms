import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([w / q, q] for q, w in zip(quality, wage))
        res = float("inf")
        heap = []    
        qsum = 0
        for r, q in workers:
            qsum += q
            heapq.heappush(heap, -q)
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * r)
        return res