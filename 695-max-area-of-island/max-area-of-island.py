class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            cur_area = 1
            s = []
            s.append((r, c))
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while s:
                row, col = s.pop()
                for rd, cr in directions:
                    r, c = row + rd, col + cr
                    if (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == 1 and
                        (r, c) not in visit):

                        s.append((r, c))
                        visit.add((r, c))
                        cur_area += 1
            
            return cur_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    print(r, c)
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res
        
    # time: O(m *  n)
    # space: 