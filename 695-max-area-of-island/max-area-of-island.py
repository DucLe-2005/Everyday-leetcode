class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # time: O(m * n)
        # space: O(m * n)
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(start_r: int, start_c: int):
            queue = deque([(start_r, start_c)])
            area = 0

            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                area += 1
                for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                    
            return area
        
        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
                
        