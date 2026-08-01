class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time: O(mn * 3L), L = len(word)
        # space: O(L)
        m, n = len(board), len(board[0])
        if m*n < len(word):
            return False

        def dfs(i: int, r: int, c: int) -> bool:
            if (r < 0 or r ==  m or 
                c < 0 or c == n or 
                board[r][c] != word[i]
            ):
                return False
            if i == len(word) - 1:
                return True
            
            char = board[r][c]
            board[r][c] = "."
            
            top = dfs(i+1, r-1, c)
            bot = dfs(i+1, r+1, c)
            left = dfs(i+1, r, c-1)
            right = dfs(i+1, r, c+1)

            board[r][c] = char
            return top or bot or left or right
        
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False

            
            

