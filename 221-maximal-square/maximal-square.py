class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1 and matrix[0][0] == "0":
            return 0
        
        max_side = 0
        dp = [] # dp[i][j]: largest square seen in the matrix that ends here
        for row in matrix:
            new_row = []
            for column in row:
                if column == "1":
                    max_side = 1
                new_row.append(int(column))
            dp.append(new_row)
        
        
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    if dp[i-1][j-1] == 0 or dp[i-1][j] == 0 or dp[i][j-1] == 0:
                        max_side = max(max_side, 1)
                        continue
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side