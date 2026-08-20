class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m - 1
        row = None
        while low <= high:
            mid = (high + low) // 2
            if target > matrix[mid][n-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                row = matrix[mid]
                break
    
        if not row:
            return False

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
