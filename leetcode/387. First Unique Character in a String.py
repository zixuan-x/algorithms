'''
bits
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen, duplicate = 0, 0
        for c in s:
            index = ord(c) - ord('a')
            musk = 1 << index
            if seen & musk > 0:
                duplicate |= musk 
            else:
                seen |= musk
        
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            musk = 1 << index
            if not duplicate & musk:
                return i
            
        return -1

'''
hash table - counter
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1


            