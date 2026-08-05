class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # time: O(m * n)
        # space: O(m * n)

        fresh = 0
        queue = deque([])
        m, n = len(grid), len(grid[0])
        rotten_oranges = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.add((i, j))
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in rotten_oranges
                    ):
                        queue.append((nr, nc))
                        rotten_oranges.add((nr, nc))
                        fresh -= 1

            if queue:    
                time += 1

        return time if fresh == 0 else -1

