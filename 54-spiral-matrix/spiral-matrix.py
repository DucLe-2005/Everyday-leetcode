class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # add all items in the top row from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # add all items in the right column from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            if not left < right or not top < bottom:
                break
            
            # add all items in the bottom row from right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # add all items in the left row from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
        
