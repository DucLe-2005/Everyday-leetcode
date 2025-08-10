class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        isUp = True
        row, col = 0, 0

        while row < m and col < n:
            if isUp:
                while row > 0 and col < n - 1:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
                res.append(mat[row][col])

                if col + 1 == n:  # move down if at the last column
                    row += 1
                else:
                    col += 1
        
            else:
                while row < m - 1 and col > 0:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                res.append(mat[row][col])

                
                if row + 1 == m:  # move right if at the last row
                    col += 1
                else:
                    row += 1
                
            isUp = not isUp

        return res