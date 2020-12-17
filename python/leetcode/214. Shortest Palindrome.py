'''
KMP:
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        mirrorString = s + '#' + s[::-1]
        table = self.preprocessing(mirrorString)
        return s[table[-1]:][::-1] + s

    def preprocessing(self, s):
        table = [0] * len(s)
        j, i = 0, 1
        while i < len(s):
            if s[j] == s[i]: # matched
                table[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = table[j - 1]
            else:
                # table[i] = 0
                i += 1
        return table

'''
TLE:
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        for end in range(len(s) - 1, -1, -1):
            i, j = 0, end
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            if i >= j:
                break
        return s[end + 1:][::-1] + s       