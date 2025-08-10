class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        res = [[0] * c for _ in range(r)]
        i = 0
        line = []
        i, j = 0, 0
        for row in mat:
            for col in row:
                if j < c:
                    res[i][j] = col
                    j += 1
        
                if j == c:
                    j = 0
                    i += 1

        return res

