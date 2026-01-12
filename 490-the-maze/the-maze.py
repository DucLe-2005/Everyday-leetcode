class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # BFS
        # Move the ball in 3 directions excluding the previous direction
        # Move the ball in that direction until hit a wall
        # Mark visited position to set "visited"
        # Add the positions to the queue (row, col, prev_direction)
        # Once the queue is empty and haven't reach the destination,
        # return False.

        # First kick the ball in 4 directions
        q = deque([(start[0], start[1])])
        dest = (destination[0], destination[1])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        visited = {(start[0], start[1])}
        m, n = len(maze), len(maze[0])
        while q:
            r, c = q.popleft()
            if (r, c) == dest:
                return True

            for dr, dc in dirs:
                nr, nc = r, c

                # The ball rolls until hitting a wall
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))

        return False
