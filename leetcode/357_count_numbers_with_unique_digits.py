class Solution:
    """
    9 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
    """
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1
        product = 1
        for i in range(n if n <= 10 else 10):
            product *= 9 if i == 0 else 10 - i
            res += product
        return res