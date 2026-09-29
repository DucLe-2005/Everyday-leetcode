class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        m, n = len(board), len(board[0])
        q = deque([click])

        while q:
            r, c = q.popleft()
            square = board[r][c]
            
            if square == 'M':
                board[r][c] = 'X'
                break
            elif square == 'E':
                mines = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and 
                        0 <= nc < n and
                        board[nr][nc] == 'M'
                    ):
                        mines += 1
                
                if mines > 0:
                    board[r][c] = str(mines)
                else:
                    board[r][c] = 'B'
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < m and 
                            0 <= nc < n and
                            board[nr][nc] == 'E'
                        ):
                            q.append([nr, nc])
        
        return board