class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = []
        for _ in range(m + 1):
            dp.append([float("inf")] * (n + 1))

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n -1:
                    dp[i][j] = grid[i][j]
                else:  
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        
        return dp[0][0]

