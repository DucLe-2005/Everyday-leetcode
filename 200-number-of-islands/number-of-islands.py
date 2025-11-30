class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        q = deque()
        islands = 0

        def bfs():
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                x, y = q.popleft()
                print((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx not in range(len(grid)) or ny not in range(len(grid[0])):
                        continue
                    if grid[nx][ny] == "1" and (nx, ny) not in visit:
                        q.append((nx, ny))
                        visit.add((nx, ny))
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    q.append((i, j))
                    visit.add((i, j))
                    bfs()
                    islands += 1
        
        return islands
