class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        intersections = []
        
        i, j, start, end = 0, 0, 0, 1
        while i < len(A) and j < len(B):
            new_start = max(A[i][start], B[j][start])
            new_end = min(A[i][end], B[j][end])
            
            if new_start <= new_end:
                intersections.append([new_start, new_end])
                
            if A[i][end] < B[j][end]:
                i += 1
            else:
                j += 1

        return intersections