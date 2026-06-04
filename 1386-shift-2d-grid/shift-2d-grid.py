class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for _ in range(k):
            prev = grid[m-1][n-1]
            for i in range(m):
                for j in range(n):
                    tmp = grid[i][j]
                    grid[i][j] = prev
                    prev = tmp
        
        return grid
