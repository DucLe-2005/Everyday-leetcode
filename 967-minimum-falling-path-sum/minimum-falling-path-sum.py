class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix.copy()
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                path = dp[i-1][j]

                if j - 1 >= 0:
                    path = min(path, dp[i-1][j-1])
                if j + 1 < n:
                    path = min(path, dp[i-1][j+1])

                dp[i][j] += path
        return min(dp[-1])