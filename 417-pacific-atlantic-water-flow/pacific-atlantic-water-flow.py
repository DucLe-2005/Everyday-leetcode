class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # run dfs on the top and left sides to mark all positions that can flow to the pacific ocean; record visited positions to a set
        # run dfs on the bottom and right sides to mark all positions that can flow to the atlantic ocean; record visited positions to a set
        # the poisitions that can flow to both oceans are the ones that are on both sets.
        # time: O(m * n)
        # space: O(m * n)
    
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if r not in range(m) or c not in range(n) or (r, c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))
            cur_height = heights[r][c]

            dfs(r + 1, c, visit, cur_height)
            dfs(r - 1, c, visit, cur_height) 
            dfs(r, c + 1, visit, cur_height) 
            dfs(r, c - 1, visit, cur_height) 

        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n - 1])
        
        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])
        
        res = []
        for r, c in pac:
            if (r, c) in atl:
                res.append([r, c])
        
        return res
        

        