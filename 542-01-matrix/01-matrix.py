class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 1. multi-source bfs
        m, n = len(mat), len(mat[0])
        matrix = [row[:] for row in mat]
        seen = set()
        q = collections.deque()

        # add all O's to the queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))

        def valid(x, y):
            return nx in range(m) and ny in range(n) and (nx, ny) not in seen and mat[nx][ny] == 1

        # bfs simultaneously from O's
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        level = 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if valid(nx, ny):
                        q.append((nx, ny))
                        matrix[nx][ny] = level
                        seen.add((nx, ny))
            
            if q:
                level += 1

        return matrix
