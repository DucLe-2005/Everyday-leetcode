class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # create a 2D array where array[i][j] is the total number of ways to get to the corner if we start at this position
        # iterate right to left, bottom to top, and update the 2D array
        # the answer is at dp[0][0] where the robot is staying
        # edge case: the obstacle is either at the robot's position or at the down right corner
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # Determine if the last row can reach the destination
        obs_seen = False
        for i in range(n - 2, -1, -1):
            if obs_seen:
                dp[m - 1][i] = 0
                continue
            if obstacleGrid[m - 1][i] == 1:
                obs_seen = True
                dp[m - 1][i] = 0
            
        obs_seen = False
        # Determine if the last column can reach the destination
        for i in range(m - 2, -1, -1):
            if obs_seen:
                dp[i][n - 1] = 0
                continue
            if obstacleGrid[i][n - 1] == 1:
                obs_seen = True
                dp[i][n - 1] = 0
        
        print(dp)
        
        for i in range(m - 2, -1, - 1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                else:
                    dp[i][j] = 0
        
        return dp[0][0]

