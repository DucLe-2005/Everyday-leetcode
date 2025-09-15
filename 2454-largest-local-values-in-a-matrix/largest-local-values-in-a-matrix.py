class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        
        def helper(x, y):
            num = 0
            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    num = max(num, grid[i][j])
            return num

        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = helper(j, i)

        return res
        