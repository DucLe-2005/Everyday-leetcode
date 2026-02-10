class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # iterate click
        # if pressed empty square, check 9 adjacent squares for hidden bombs
        # update the square with the number of bombs, or B if 0 adjacent bomb
        # if pressed bomb, update the square to 'X'
        surroundings = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        m, n = len(board), len(board[0])
        r, c = click

        # Step on mine, return board
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        def count_adjacent_mines(r, c):
            mines = 0
            for dr, dc in surroundings:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    mines += 1
            return mines


        board[r][c] = 'B'
        q = deque([[r, c]])

        while q:
            r, c = q.popleft()
            mines = count_adjacent_mines(r, c)

            if mines > 0:
                board[r][c] = str(mines)
                continue

            for dr, dc in surroundings:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                    board[nr][nc] = 'B'
                    q.append([nr, nc])

        return board
