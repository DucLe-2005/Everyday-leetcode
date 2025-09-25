class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # check all sides of the board
        # add all 'O' to a queue
        # use dfs on on all 'O' in the queues to find regions that are not surrounded, mark those positions as open
        # iterate each position on the board to translate 'O' to 'X', except those that are marked as 'open'

        # time: O(m * m)
        # space: O(m * n)
    
        m, n = len(board), len(board[0])
        isSurrounded = [[True] * n for _ in range(m)]

        def dfs(i, j):
            if i not in range(m) or j not in range(n) or board[i][j] != 'O' or not isSurrounded[i][j]:
                return
            isSurrounded[i][j] = False
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1) 

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n-1)
        
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and isSurrounded[r][c]:
                    board[r][c] = 'X'
        