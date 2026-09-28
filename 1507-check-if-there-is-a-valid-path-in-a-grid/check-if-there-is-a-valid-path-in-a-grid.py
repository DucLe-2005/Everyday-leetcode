class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)

        dirs = {
            1: [LEFT, RIGHT],
            2: [UP, DOWN],
            3: [LEFT, DOWN],
            4: [RIGHT, DOWN],
            5: [UP, LEFT],
            6: [UP, RIGHT]
        }

        opposite = {
            UP: DOWN,
            DOWN: UP,
            LEFT: RIGHT,
            RIGHT: LEFT,
        }

        visited = set()

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return True
            
            visited.add((r, c))

            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                
                if opposite[(dr, dc)] not in dirs[grid[nr][nc]]:
                    continue
                
                if dfs(nr, nc):
                    return True
            
            return False
    
        return dfs(0, 0)