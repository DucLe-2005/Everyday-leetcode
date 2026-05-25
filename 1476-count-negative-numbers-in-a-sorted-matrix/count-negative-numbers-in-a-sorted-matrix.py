class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # tim: O(m * n)
        # space: O(1)
        res = 0

        for i in range(len(grid) -1, -1, -1):
            row = grid[i]
            for j in range(len(row) - 1, -1, -1):
                if row[j] >= 0:
                    break
                res += 1
    
        return res