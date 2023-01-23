class Solution:
    """
    can also check if B in (A + A)
    """
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if not A or not B:
            return True
        
        n = len(A)
        for i in range(n):
            if B[i] != A[0]: continue
            for j in range(n):
                if A[j] != B[(i + j) % n]:
                    break
                if j == n - 1:
                    return True
        
        return False
                