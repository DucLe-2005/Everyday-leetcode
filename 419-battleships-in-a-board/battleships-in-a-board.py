class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # do a dfs once find a bpat
        # convert all x's to '.' as you interate through it
        # once reach the end of a dfs path, increment the answer variable by 1

        count = 0
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            board[i][j] = '.'
            if i + 1 < m and board[i+1][j] == 'X':
                dfs(i+1, j)
            if i > 0 and board[i-1][j] == 'X':
                dfs(i-1, j)
            if j > 0 and board[i][j-1] == 'X':
                dfs(i, j-1)
            if j + 1 < n and board[i][j+1] == 'X':
                dfs(i, j+1)
            
            return 1


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    count += dfs(i, j)
        
        return count