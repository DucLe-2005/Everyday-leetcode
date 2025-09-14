class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        res = []
        isUp = True
        row, col = 0, 0

        while row < n and col < m:
            if isUp:
                while row > 0 and col < m - 1:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
                res.append(mat[row][col])

                # go down if reach the last column else go right
                if col + 1 == m:
                    row += 1
                else:
                    col += 1
            else:
                while row < n - 1 and col > 0:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                res.append(mat[row][col])

                # go right if reach the last row else go down
                if row + 1 == n:
                    col += 1
                else:
                    row += 1

            isUp = not isUp
        
        return res

