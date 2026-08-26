class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # time: O(m * n)
        # space: O(m * n)

        m, n = len(grid), len(grid[0])

        dp = grid.copy()
        for i in range(m - 2, -1, -1):
            dp[i][n-1] += dp[i+1][n-1]
        
        for j in range(n - 2, -1, -1):
            dp[m-1][j] += dp[m-1][j+1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] += min(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]