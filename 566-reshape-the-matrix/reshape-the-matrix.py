class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat
        
        new_mat = [[] for _ in range(r)]
        row, col = 0, 0
        for i in range(m):
            for j in range(n):
                new_mat[row].append(mat[i][j])
                col += 1

                if col == c:
                    row += 1
                    col = 0
        
        return new_mat
