class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result, n = 0, len(s)
        for i in range(n):
            c = s[i]
            if i < n - 1 and mapping[c] < mapping[s[i + 1]]:
                result -= mapping[c]
            else:
                result += mapping[c]
            print(result)
        return result