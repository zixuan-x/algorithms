class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26 # You may assume the string contains only lowercase alphabets.
        for c in s:
            counter[ord(c) - 97] += 1
        for c in t:
            counter[ord(c) - 97] -= 1
        for count in counter:
            if count:
                return False
        return True