class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - 2) for _ in range(n - 2)]

        def helper(r, c):
            largest = grid[r][c]
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    largest = max(largest,  grid[i][j])
            
            return largest
        
        for i in range(m - 2):
            for j in range(n - 2):
                res[i][j] = helper(i, j)
        
        return res