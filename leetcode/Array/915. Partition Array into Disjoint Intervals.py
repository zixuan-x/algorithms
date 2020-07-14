''' 1. 3 passes '''
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)

        leftmax = [A[0]] * n
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], A[i])
            
        rightmin = [A[-1]] * n
        for i in range(n - 2, -1, -1):
            rightmin[i] = min(rightmin[i + 1], A[i])
        
        for i in range(n - 1):
            if leftmax[i] <= rightmin[i + 1]:
                return i + 1

''' 2. 2 passes '''
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
            
        rightmin = [A[-1]] * n
        for i in range(n - 2, -1, -1):
            rightmin[i] = min(rightmin[i + 1], A[i])
        
        leftmax = float('-inf')
        for i in range(n - 1):
            leftmax = max(leftmax, A[i])
            if leftmax <= rightmin[i + 1]:
                return i + 1

''' 3. 1 pass '''
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        partitionMax, partitionIdx, maxSoFar = A[0], 0, A[0]
        for i in range(len(A)):
            maxSoFar = max(maxSoFar, A[i])
            if A[i] < partitionMax:
                partitionIdx = i
                partitionMax = maxSoFar
        return partitionIdx + 1
        