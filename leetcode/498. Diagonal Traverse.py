'''
1. brute force
time complexity:
space complexity:
'''
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        diagonals = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diagonals[i + j].append(matrix[i][j])
        
        for k in sorted(diagonals):
            if k % 2 == 0:
                diagonals[k].reverse()
            result += diagonals[k]
        
        return result

'''
2. The order of if/else statements in the moving up/moving down blocks matters
time complexity: O(m * n)
space complexity: O(1) without considering space for return value
'''
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = [0] * (m * n) 
        
        r, c = 0, 0
        for i in range(m * n):
            result[i] = matrix[r][c]
            if (r + c) % 2 == 0:  # moving up
                if c == n - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:                 # moving down
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        
        return result

