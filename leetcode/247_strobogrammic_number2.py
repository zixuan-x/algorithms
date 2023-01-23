class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = ['']
        if n % 2 != 0:
            res = ['0', '1', '8']
        for i in range(n // 2):
            newRes = []
            for cur in res:
                if i != n // 2 - 1:
                    newRes.append('0' + cur + '0')
                newRes.append('1' + cur + '1')
                newRes.append('6' + cur + '9')
                newRes.append('8' + cur + '8')
                newRes.append('9' + cur + '6')
            res = newRes
        
        return res
                
                    