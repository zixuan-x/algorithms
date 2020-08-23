class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = defaultdict(list)
        i, row = 0, 0
        while i < len(s):
            # go down
            row = 0
            while i < len(s) and row < numRows:
                rows[row].append(s[i])
                i += 1
                row += 1
            
            # go up
            row = numRows - 2
            while i < len(s) and row > 0:
                rows[row].append(s[i])
                i += 1
                row -= 1
        return ''.join(c for r in sorted(rows) for c in rows[r])
        