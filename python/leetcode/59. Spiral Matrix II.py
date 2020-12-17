class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        
        matrix = [[0] * n for _ in range(n)]
        i = 1
        r, c = 0, 0
        while i <= n * n:
            # go right
            while c < n and matrix[r][c] == 0:
                matrix[r][c] = i
                i += 1
                c += 1
            c -= 1
            r += 1
            # go down
            while r < n and matrix[r][c] == 0:
                matrix[r][c] = i
                i += 1
                r += 1
            r -= 1
            c -= 1
            # go left
            while c >= 0 and matrix[r][c] == 0:
                matrix[r][c] = i
                i += 1
                c -= 1
            c += 1
            r -= 1
            # go up
            while r >= 0 and matrix[r][c] == 0:
                matrix[r][c] = i
                i += 1
                r -= 1
            r += 1
            c += 1
        return matrix