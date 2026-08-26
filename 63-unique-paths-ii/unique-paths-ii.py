class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i + 1 < m:
                        dp[i][j] += dp[i+1][j]
                    if j + 1 < n:
                        dp[i][j] += dp[i][j+1]
        
        return dp[0][0]