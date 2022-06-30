class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < A[mid + 1]:
                left = mid
            else:
                right = mid
        return left if A[left] > A[right] else right