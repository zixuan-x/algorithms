from heapq import heappush, heappop

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

'''
sort all:
time: O(nlogn)
space:
'''
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([interval for employee in schedule for interval in employee], key=lambda x: x.start)
        freeTimes, merged = [], intervals[0].end
        for interval in intervals:
            if interval.start <= merged:
                merged = max(merged, interval.end)
            else:
                freeTimes.append(Interval(merged, interval.start))
                merged = interval.end
        return freeTimes

'''
Time Complexity: O(N * logK)
Space Complexity: O(K)
'''
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule:
            return []
        
        n = len(schedule)
        result = []   # [intervals] 
        minHeap = []  # [(interval.start, employeeIndex, intervalIndex)]
        for i in range(n):
            heappush(minHeap, (schedule[i][0].start, i, 0))
        
        previousInterval = schedule[minHeap[0][1]][minHeap[0][2]]
        while minHeap:
            _, employeeIndex, intervalIndex = heappop(minHeap)
            currentInterval = schedule[employeeIndex][intervalIndex]
            if previousInterval.end < currentInterval.start:
                result.append(Interval(previousInterval.end, currentInterval.start))
                previousInterval = currentInterval
            else:
                if previousInterval.end < currentInterval.end:
                    previousInterval = currentInterval
            
            if intervalIndex + 1 < len(schedule[employeeIndex]):
                heappush(minHeap, (schedule[employeeIndex][intervalIndex + 1].start, employeeIndex, intervalIndex + 1))
        
        return result