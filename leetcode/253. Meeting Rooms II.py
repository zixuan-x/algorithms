class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        for interval in intervals:
            if minHeap and minHeap[0] <= interval[0]:
                heapq.heapreplace(minHeap, interval[1])
            else:
                heapq.heappush(minHeap, interval[1])
        return len(minHeap)