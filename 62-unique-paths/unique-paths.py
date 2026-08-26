class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # all the cells at the bottom have 1 way to reach star
        # all the cells at the rght side have 1 way to reach star
        # dp[i][j] += dp[i+1][j] + dp[i][j+1]
        # time: O(m+n)
        # space: O(m+n)

        dp = [[1] * n for _ in range(m)]
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]