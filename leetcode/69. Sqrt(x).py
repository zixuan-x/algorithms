class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left + 1 < right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid
            else:
                right = mid
        if right * right <= x:
            return right
        else:
            return left