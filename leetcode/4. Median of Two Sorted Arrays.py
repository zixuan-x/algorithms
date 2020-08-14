class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        A, B = nums1, nums2
        if m > n:
            A, B, m, n = B, A, n, m
        # You may assume nums1 and nums2 cannot be both empty.
        left, right = 0, m
        half = (m + n + 1) // 2
        while left <= right:
            x = (left + right) // 2
            y = half - x
            if x < m and B[y - 1] > A[x]:
                # i is too small, must increase it
                left = x + 1
            elif x > 0 and A[x - 1] > B[y]:
                # i is too big, must decrease it
                right = x - 1
            else:
                if x == 0:
                    maxOfLeft = B[y - 1]
                elif y == 0:
                    maxOfLeft = A[x - 1]
                else:
                    maxOfLeft = max(A[x - 1], B[y - 1])
                
                if (m + n) % 2:
                    return maxOfLeft
                
                if x == m: 
                    minOfRight = B[y]
                elif y == n: 
                    minOfRight = A[x]
                else: 
                    minOfRight = min(A[x], B[y])
                    
                return (maxOfLeft + minOfRight) / 2.0
                    
                