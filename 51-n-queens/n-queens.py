class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # time: O(n * n! + S * n^2), S = number of valid chess board
        # space: O(n^2)
        res = []
        cols = set()
        diag1 = set() # top left to bottom right
        diag2 = set()  # top right to bottom left
        board = [['.'] * n for _ in range(n)]
        print(board)

        def dfs(r: int) -> None:
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                dfs(r + 1)

                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        dfs(0)
        return res

