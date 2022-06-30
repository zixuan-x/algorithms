import collections
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = []
        for task, times in counter.items():
            heapq.heappush(heap, (-times, task))
        
        count = 0
        while heap:
            tempList = []
            k = n + 1
            while k > 0 and heap:
                cur = heapq.heappop(heap)
                tempList.append(cur)
                k -= 1
                count += 1
            
            while tempList:
                times, task = tempList.pop()
                if times < -1:
                    heapq.heappush(heap, (times + 1, task))
            
            if heap:
                count += k
        
        return count
            
        