class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time: O(m + n)
        # space: O(1)

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        
        return False