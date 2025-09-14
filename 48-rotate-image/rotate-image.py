class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left, right = 0, n - 1

        while left < right:
            top, bottom = left, right

            for i in range(right - left):
                # save top left
                top_left = matrix[top][left + i]

                # bottom left -> top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom right -> bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top right -> bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
            
                # top left -> top right
                matrix[top + i][right] = top_left
            
            left += 1
            right -= 1
        

