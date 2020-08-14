'''
brute force 1:
# generate all substrings -> O(n ^ 2)
for -> :
    for -> :
        check palindormic for each string -> O(n)
time: O(n ^ 3)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if sub != sub[::-1]:
                    continue
                if len(sub) > len(result):
                    result = sub
        return result

'''
two pointers:
for -> s:  
    1. left = right = i
    2. left = i, right = i + 1
time: O(n ^ 2)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            sub = self.find(s, i, i)
            if len(sub) > len(result):
                result = sub
            if i < len(s) - 1:
                sub = self.find(s, i, i + 1)
                if len(sub) > len(result):
                    result = sub
        return result
            
    def find(self, s, l, r):
        length = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]