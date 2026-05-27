class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # time: O(m * n)
        # space: O(m + n)
        m, n = len(grid), len(grid[0])
        row_count = [sum(row) for row in grid]
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                col_count[j] += grid[i][j]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row_count[i] > 1 or col_count[j] > 1):
                    res += 1
        
        return res
        
