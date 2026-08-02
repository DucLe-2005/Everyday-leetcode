class Solution:
    def totalNQueens(self, n: int) -> int:
        # time: O(n * n!)
        # space: O(n)
        
        cols = set()
        diag1 = set()
        diag2 = set()
        res = 0

        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                
                dfs(r + 1)
                
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
        
        dfs(0)
        return res