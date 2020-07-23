class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True  
          
        while num >= 2 and num % 2 == 0:
            num /= 2;  
        while num >= 3 and num % 3 == 0:
            num /= 3;  
        while num >= 5 and num % 5 == 0:
            num /= 5;  
          
        return num == 1


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 1:
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                return False
        return True