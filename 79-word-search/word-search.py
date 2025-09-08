class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def dfs(i, j, idx):
            if board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            
            idx += 1
            tmp = board[i][j]
            board[i][j] = '#'
            
            if i > 0 and dfs(i - 1, j, idx):  # up
                board[i][j] = tmp
                return True
            if i < n - 1 and dfs(i + 1, j, idx):  # down
                board[i][j] = tmp
                return True
            if j > 0 and dfs(i, j - 1, idx):  # left
                board[i][j] = tmp
                return True
            if j < m - 1 and dfs(i, j + 1, idx):
                board[i][j] = tmp
                return True
            
            # backtrack
            board[i][j] = tmp
            return False
        
        # pruning: return immediately if grid's size is smaller than word's length
        if n * m < len(word):
            return False


        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False