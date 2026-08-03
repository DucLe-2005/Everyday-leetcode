class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # time: O(m*n)
        # space: O(m*n)
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(r: int, c: int) -> int:
            if (r < 0 or r == m or
                c < 0 or c == n or
                grid[r][c] == 0):
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
        
            return (
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        return 0
        

