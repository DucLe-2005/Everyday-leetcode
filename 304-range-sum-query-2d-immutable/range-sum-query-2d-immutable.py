class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # sumMatrix[i][j] = sum matrix from matrix[0][0] to matrix[i-1][j-1]
        self.sumMatrix = [[0] * (COLS + 1) for _  in range(ROWS + 1)]
        for i in range(ROWS):
            prefix = 0
            for j in range(COLS):
                prefix += matrix[i][j]
                above = self.sumMatrix[i][j+1]
                self.sumMatrix[i+1][j+1] = prefix + above
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.sumMatrix[row2+1][col2+1]
        left = self.sumMatrix[row2+1][col1]
        above = self.sumMatrix[row1][col2+1]
        top_left = self.sumMatrix[row1][col1]
        return matrix - left - above + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)