class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in range(len(matrix)):
            curVal = 0
            curRow = []
            for n in matrix[i]:
                curVal += n
                curRow.append(curVal)
            self.prefix.append(curRow)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            rightSum = self.prefix[i][col2]
            leftSum = self.prefix[i][col1 - 1] if col1 - 1 >= 0 else 0
            sum += rightSum - leftSum
        
        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)