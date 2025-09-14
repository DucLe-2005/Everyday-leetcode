class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        res = [[] for _ in range(r)]
        row, col = 0, 0
        for i in range(m):
            for j in range(n):
                res[row].append(mat[i][j])
                col += 1
                
                if col == c:  # current row is filled
                    col = 0
                    row += 1
        
        return res

