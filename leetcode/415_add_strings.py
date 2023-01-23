class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addHelper(num1, num2)
        else:
            return self.addHelper(num2, num1)
        
    def addHelper(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        carry = 0
        res = ""
        i = 0
        while i < n1:
            index1 = n1 - 1 - i
            index2 = n2 - 1 - i
            int1 = int(num1[index1])
            int2 = int(num2[index2])
            temp = int1 + int2 + carry
            cur = temp % 10
            carry = temp // 10
            res = str(cur) + res
            i += 1
        
        while i < n2:
            index2 = n2 - 1 - i
            int2 = int(num2[index2])
            temp = int2 + carry
            cur = temp % 10
            carry = temp // 10
            res = str(cur) + res
            i += 1
        
        if carry != 0:
            res = str(carry) + res
        
        return res