class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals     

        intervals.sort()
        merged = []
        for interval in intervals:
            if merged and merged[-1][-1] >= interval[0]:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
            else:
                merged.append(interval)
        return merged

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        start, end, top = 0, 1, -1
        intervals.sort()
        for interval in intervals:
            if merged and interval[start] <= merged[top][end]:
                merged[top][end] = max(merged[top][end], interval[end])
            else:
                merged.append(interval)
        return merged