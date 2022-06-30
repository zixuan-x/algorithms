'''
Every time you need to start a meeting, 
you try to search through all existing rooms and see if there's an empty one,
if you couldn't find one,
open a new room
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []  # stores the end time of intervals
        start, end = 0, 1
        for interval in intervals:
            if not minHeap or interval[start] < minHeap[0]:
                heappush(minHeap, interval[end])
            else:
                # heapreplace(minHeap, interval[end])
                heappop(minHeap)
                heappush(minHeap, interval[end])
        return len(minHeap)