'''
sort the intervals!
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals     

        intervals.sort()
        merged, start, end = [], 0, 1
        for interval in intervals:
            if not merged or merged[-1][end] < interval[start]:
                merged.append(interval)
            else:
                merged[-1][end] = max(merged[-1][end], interval[end])
        return merged