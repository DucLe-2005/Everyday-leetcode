class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a 2D array with dimensions m x n
        # let the last row of the 2D array be all 1
        # this is because there is only one way for each at the last row to reach the corner by going right  
        # iterate right to left, bottom to top
        # the number of ways to get the corner at each position equals to the sum
        # of the number of ways to get to the corner starting at the position to the right and position below
        # the answer will be the first number in the first array of the 2D array
        # time: O(m * n), space: O(m * n)

        path_sums = [[1 for _ in range(n)] for i in range(m)]
        print(path_sums)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                path_sums[i][j] = path_sums[i + 1][j] + path_sums[i][j + 1]
        
        return path_sums[0][0]
