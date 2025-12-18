class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        while True:
        # Mark all cells to crush
            crush = [[False] * n for _ in range(m)]
            has_crush = False

            # Horizontal
            for i in range(m):
                for j in range(n - 2):
                    if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i][j+2]:
                        crush[i][j] = crush[i][j+1] = crush[i][j+2] = True
                        has_crush = True

            # Vertical
            for j in range(n):
                for i in range(m - 2):
                    if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j]:
                        crush[i][j] = crush[i+1][j] = crush[i+2][j] = True
                        has_crush = True
            
            if not has_crush:
                break
            
            # Crush marked cells
            for i in range(m):
                for j in range(n):
                    if crush[i][j]:
                        board[i][j] = 0
            
            # Drop candies
            for j in range(n):
                write_index = m - 1

                for i in range(m - 1, -1, -1):
                    if board[i][j] != 0:
                        board[write_index][j] = board[i][j]
                        write_index -= 1

                while write_index >= 0:
                    board[write_index][j] = 0
                    write_index -= 1
        
        return board
