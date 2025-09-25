class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31 - 1
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()

        # push all gates into the queue
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r, c))
        
        # BFS from all gates simultaneously
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # only expand into empty rooms (INT)
                if (nr in range(m) and nc in range(n) and rooms[nr][nc] == INF):
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))

            
