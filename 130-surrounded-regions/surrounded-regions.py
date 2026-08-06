class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # time: O(m * n)
        # space: O(m * n)
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int) -> bool:
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                board[r][c] != 'O'
            ):
                return

            board[r][c] = 'T'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Mark all 'O' connected to left and right borders
        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)
        
        # Mark all 'O' connected to top and bottom borders
        for col in range(n):
            dfs(0, col)
            dfs(m - 1, col)

        # Convert all 'O' to 'X', 'T' to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        