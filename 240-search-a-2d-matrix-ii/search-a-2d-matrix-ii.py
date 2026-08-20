class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for row in matrix:
            l, r = 0, n - 1

            while l <= r:
                m = (l + r) // 2

                if row[m] == target:
                    return True
                elif row[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            
        return False