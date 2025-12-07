class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        def dfs(row, col):
            if row == 0 and col == 0:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            
            paths = 0
            if row > 0 and obstacleGrid[row - 1][col] == 0:
                paths += dfs(row - 1, col)
            if col > 0 and obstacleGrid[row][col - 1] == 0:
                paths += dfs(row, col - 1)

            memo[(row, col)] = paths
            return paths
        
        memo = {}
        return dfs(m - 1, n - 1)

