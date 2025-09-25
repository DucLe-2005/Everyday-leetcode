class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # check all sides of the board
        # add all 'O' to a queue
        # use bfs on on all 'O' in the queues to find regions that are not surrounded, mark those positions as open
        # iterate each position on the board to translate 'O' to 'X', except those that are marked as 'open'

        # time: O(m * m)
        # space: O(m * n)
    
        m, n = len(board), len(board[0])
        not_captured = set()

        q = collections.deque()  # add 'O' on the sides to queue
        for r in range(m):
            if board[r][0] == 'O':
                q.append((r, 0))
                not_captured.add((r, 0))
            if board[r][n - 1] == 'O':
                q.append((r, n - 1))
                not_captured.add((r, n - 1))
        
        for c in range(n):
            if board[0][c] == 'O':
                q.append((0, c))
                not_captured.add((0, c))
            if board[m - 1][c] == 'O':
                q.append((m - 1, c))
                not_captured.add((m - 1, c))
                

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                print(nr, nc)
                if (nr in range(m) and
                    nc in range(n) and 
                    (nr, nc) not in not_captured and 
                    board[nr][nc] == 'O'):
                    not_captured.add((nr, nc))
                    q.append((nr, nc))
        
        for r in range(m):
            for c in range(n):
                if (r, c) not in not_captured:
                    board[r][c] = 'X'

        


        
        
