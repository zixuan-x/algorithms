class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0 :
            return 1.0 / self.power(x, -n)
        else:
            return self.power(x, n)
    
    def power(self, x, n):
        if n == 0: return 1
        # n > 0
        half = self.power(x, n // 2)
        if n & 1:
            return x * half * half
        else:
            return half * half
        