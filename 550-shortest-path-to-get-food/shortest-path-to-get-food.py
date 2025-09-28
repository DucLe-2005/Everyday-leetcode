class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # put all #'s into a queue
        # conduct a bfs simultaneously on all the food
        # each time we expand out, the lenght increments by 1.
        # if we reached "*", then return the length.
        # if the queue is still empty, the return -1.

        m, n = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()

        # put all food's locations to the queue
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '#':
                    q.append((r, c))

        # bfs simultaneously starting from all food's locations
        length = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                        if grid[nr][nc] == '*':
                            return length + 1
                        elif grid[nr][nc] == 'O':
                            q.append((nr, nc))
                            seen.add((nr, nc))
            
            length += 1
            
        return -1


        
