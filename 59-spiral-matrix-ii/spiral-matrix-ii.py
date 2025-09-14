class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    # create a n*n matrix
    # keep boundaries and traverse through the matrix in spiral order
    # go top row from right to left, the right column from top to bottom, bottom from right to left, and left column from bottom to top
    # add number to each block and then increase the number so the next block has a higher number
        a = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n

        while left < right and top < bottom:
            # top row: left to right
            for i in range(left, right, 1):
                matrix[top][i] = a
                a += 1
            top += 1

            # right column: top to bottom
            for i in range(top, bottom, 1):
                matrix[i][right - 1] = a
                a += 1
            right -= 1

            if not left < right or not top < bottom:
                break
            
            # bottom row: right to left
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = a
                a += 1
            bottom -= 1

            # left column: bottom to top
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = a
                a += 1
            left += 1
        
        return matrix