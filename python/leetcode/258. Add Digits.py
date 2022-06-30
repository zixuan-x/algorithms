class Solution:
    def addDigits(self, num: int) -> int:
        if num < 0:
            return -1
        while num > 9:
            digitSum = 0
            while num > 0:
                digitSum += num % 10
                num //= 10
            num = digitSum
        return num