'''
A[i][j] on the same diagonal have same value of i - j
For each diagonal,
put its elements together, sort, and set them back.

从左上到右下的对角线：i - j 相等
从右上到左下的对角线：i + j 相等
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
                
        for k in diagonals:
            diagonals[k].sort(reverse=True)
            
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        
        return mat