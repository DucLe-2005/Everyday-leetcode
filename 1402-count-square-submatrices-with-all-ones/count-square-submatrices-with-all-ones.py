class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = matrix.copy()
        squares = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return sum(sum(row) for row in dp)
