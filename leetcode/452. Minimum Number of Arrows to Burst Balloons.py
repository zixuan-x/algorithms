class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        start, end = 0, 1
        arrowPos = points[0][end]
        count = 1
        for i in range(len(points)):
            if points[i][start] <= arrowPos:
                continue
            else:
                arrowPos = points[i][end]
                count += 1
        return count