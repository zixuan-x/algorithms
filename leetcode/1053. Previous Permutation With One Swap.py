class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        i = len(A) - 1
        while i > 0:
            if A[i - 1] > A[i]:
                break
            i -= 1
        
        if i == 0:
            return A
        
        j = i - 1
        i = len(A) - 1
        
        while i > j:
            if A[i] < A[j] and A[i - 1] != A[i]:
                A[i], A[j] = A[j], A[i]
                break
            i -= 1
        return A