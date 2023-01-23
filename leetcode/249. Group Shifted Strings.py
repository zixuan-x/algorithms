class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifts = defaultdict(list)
        for s in strings:
            sequence = []
            for i in range(len(s) - 1):
                diff = (ord(s[i + 1]) - ord(s[i]) + 26) % 26
                sequence.append(diff)
            shifts[tuple(sequence)].append(s)
        result = []
        for k in shifts:
            result.append(shifts[k])
        return result