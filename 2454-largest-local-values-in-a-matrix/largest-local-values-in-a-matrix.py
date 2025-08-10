class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        res = [[0] * (n-2) for _ in range(m-2)]
        for i in range(m - 2):
            for j in range(n - 2):
                
                max_val = 0
                # from top left, check the 3x3 matrix
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        max_val = max(max_val, grid[a][b])
                
                res[i][j] = max_val

        return res
