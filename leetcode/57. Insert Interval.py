'''
time: O(n)
space: O(n)
必须新创建一个list，否则每次merge都得delete，时间复杂度变为O(n ^ 2)
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        start, end = 0, 1
        i = 0
        # add all the intervals ending before newInterval starts
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1
        # merge all overlapping intervals to one considering newInterval
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1
        merged.append(newInterval)
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged

'''
time: O(n)
space: O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        
        # O(n) time
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)
        
        # O(n) time, O(n) space
        merged = []
        for interval in intervals:
            if merged and merged[-1][-1] >= interval[0]:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
            else:
                merged.append(interval)
        return merged
        