class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate each cell in board
        # if cell == word[0]: dfs, backtrack if one way return False
        # if one dfs return True, return True
        # time: (m^2 * n^2)
        visiting = set()
        m, n = len(board), len(board[0])
        def backtrack(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row == m or col < 0 or col == n:
                return False
            if (row, col) in visiting:
                return False
            if board[row][col] != word[i]:
                return False
            
            
            visiting.add((row, col))
            found = (
                backtrack(row+1, col, i+1) or
                backtrack(row-1, col, i+1) or
                backtrack(row, col+1, i+1) or
                backtrack(row, col-1, i+1)
            )
            visiting.remove((row, col))
            
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

