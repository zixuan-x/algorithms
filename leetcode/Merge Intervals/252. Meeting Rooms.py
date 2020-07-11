class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        start, end = 0, 1
        for i in range(len(intervals) - 1):
            if intervals[i][end] > intervals[i + 1][start]:
                return False
        return True