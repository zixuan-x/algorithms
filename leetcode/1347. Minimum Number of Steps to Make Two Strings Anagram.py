'''
Analysis:
Time: O(n), space: O(n), where n = s.length() + t.length().
'''
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        return sum(abs(c1[c] - c2[c]) for c in string.ascii_lowercase) // 2

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter = Counter(s)
        count = 0
        for c in t:
            if counter[c] > 0:
                counter[c] -= 1
            else:
                count += 1
        return count