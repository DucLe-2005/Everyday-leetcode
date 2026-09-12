class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        while True:
            crushed = True

            for i in range(m):
                for j in range(n - 2):
                    if board[i][j] == 0:
                        continue

                    value = abs(board[i][j])

                    if value == abs(board[i][j+1]) == abs(board[i][j+2]):
                        board[i][j] = -value
                        board[i][j+1] = -value
                        board[i][j+2] = -value
                        crushed = False

            for j in range(n):
                for i in range(m - 2):
                    if board[i][j] == 0:
                        continue
                    
                    value = abs(board[i][j])

                    if value == abs(board[i+1][j]) == abs(board[i+2][j]):
                        board[i][j] = -value
                        board[i+1][j] = -value
                        board[i+2][j] = -value
                        crushed = False
            
            if crushed:
                return board
            
            for c in range(n):
                write = m - 1

                for r in range(m - 1, -1, -1):
                    if board[r][c] > 0:
                        board[write][c] = board[r][c]
                        write -= 1

                while write >= 0:
                    board[write][c] = 0
                    write -= 1
 


