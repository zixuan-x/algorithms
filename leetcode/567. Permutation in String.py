class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        missing = l1 = len(s1)
        for i, c in enumerate(s2):
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
            if i >= l1 and s2[i - l1] in need:
                if need[s2[i - l1]] >= 0:
                    missing += 1
                need[s2[i - l1]] += 1
            if missing == 0:
                return True
        return False