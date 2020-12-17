class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        result = 0
        negtive = False
        
        # str = str.lstrip()
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
            
        if i == len(str):
            return 0
        
        if str[i] == '-':
            negtive = True
            i += 1
        elif str[i] == '+':
            i += 1
        elif str[i].isdigit():
            pass
        else:
            return 0
        
        while i < len(str) and str[i].isdigit():
            # result = result * 10 + int(str[i])
            result = result * 10 + ord(str[i]) - ord('0')
            i += 1
            
        maxint, minint = 2 ** 31 - 1, - 2 ** 31
        
        result = result if not negtive else -result
        if result > maxint:
            return maxint
        elif result < minint:
            return minint
        else:
            return result
            
        
        