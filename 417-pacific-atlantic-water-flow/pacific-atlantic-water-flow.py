class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # time: O(m * n)
        # space: O(m * n)
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited):
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    heights[nr][nc] >= heights[r][c] and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    dfs(nr, nc, visited)
        
        for col in range(n):
            pacific.add((0, col))
            dfs(0, col, pacific)

            atlantic.add((m - 1, col))
            dfs(m - 1, col, atlantic)
        
        for row in range(m):
            pacific.add((row, 0))
            dfs(row, 0, pacific)
        
            atlantic.add((row, n - 1))
            dfs(row, n - 1, atlantic)
        
        result = []
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])
        
        return result
