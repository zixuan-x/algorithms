class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'6':'9', '0':'0', '8':'8', '1':'1', '9':'6'}
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in d or d[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True