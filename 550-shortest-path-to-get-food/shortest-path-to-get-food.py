class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()

        # put all food's locations to the queue
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '*':
                    q.append((r, c))
                    break
            if q:
                break

        # bfs simultaneously starting from all food's locations
        length = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == "#":
                    return length

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] != 'X':
                        q.append((nr, nc))
                        seen.add((nr, nc))
            
            length += 1

        return -1


        
