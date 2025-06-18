class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = 0
        COL = len(matrix[0]) - 1
        row = matrix[0]

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (r + l) // 2
            if matrix[mid][COL] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                row = matrix[mid]
                break
        
        while ROWS <= COL:
            mid = (ROWS + COL) // 2
            if row[mid] > target:
                COL = mid - 1
            elif row[mid] < target:
                ROWS = mid + 1
            else:
                return True
        
        return False
            


                

