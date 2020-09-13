class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        need = Counter(p)
        missing = m = len(p)
        result = []
        for i, c in enumerate(s):
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
            if i >= m:
                kickout = s[i - m]
                if kickout in need:
                    if need[kickout] >= 0:
                        missing += 1
                    need[kickout] += 1
            if missing == 0:
                result.append(i - m + 1)
        return result