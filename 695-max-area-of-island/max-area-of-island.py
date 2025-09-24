class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (r in range(rows) and c in range(cols) and grid[r][c] == 1):
                return 0

            grid[r][c] = 0  # mark this position as visited

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res
        
    # time: O(m *  n)
    # space: O(m * n)