class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time = 0
        rotten = set()
        queue = deque()
        m, n = len(grid), len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    rotten.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in rotten:
                        continue

                    if (
                        0 <= nr < m and
                        0 <= nc < n and 
                        grid[nr][nc] == 1
                    ):
                        queue.append([nr, nc])
                        rotten.add((nr, nc))
                        fresh -= 1
            
            if queue:
                time += 1
        
        return time if not fresh else -1