class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)
        
        merged = []
        for interval in intervals:
            if merged and merged[-1][-1] >= interval[0]:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
            else:
                merged.append(interval)
        return merged
        