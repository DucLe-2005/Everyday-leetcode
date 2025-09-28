class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # one pass: record all columns, rows that need to translate to all 0's
        # second pass: actual translation

        m, n = len(matrix), len(matrix[0])

        # Did the first row/first column originally have a zero?
        row0Zero = False
        for c in range(n):
            if matrix[0][c] == 0:
                row0Zero = True
                break

        col0Zero = False
        for r in range(m):
            if matrix[r][0] == 0:
                col0Zero = True
                break

        # Use first row/col as markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        print(matrix)

        # set cols to 0 except 1st col
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
    
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if row0Zero:
            for c in range(n):
                matrix[0][c] = 0
        if col0Zero:
            for r in range(m):
                matrix[r][0] = 0
        

        

