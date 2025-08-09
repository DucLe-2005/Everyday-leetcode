class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        a = 1
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # add numbers to the top row from left to right
            for i in range(left, right):
                matrix[top][i] = a
                a += 1
            top += 1

            # add numbers to the right column from top to bottom
            for i in range(top, bottom):
                matrix[i][right - 1] = a
                a += 1
            right -= 1

            # if not left < right or not top < bottom:
            #     break

            # add numbers to the bottom row from right to left
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = a
                a += 1
            bottom -= 1

            # add numbers to the right column from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = a
                a += 1
            left += 1

        return matrix
