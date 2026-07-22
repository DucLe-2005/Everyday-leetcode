class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time: O(mn * 3^L)
        # space: O(L)
        rows = len(board)
        cols = len(board[0])

        # not enough cells
        if len(word) > rows * cols:
            return False
        
        # not enough required characters
        board_count = Counter(
            board[r][c]
            for r in range(rows)
            for c in range(cols)
        )

        word_count = Counter(word)
        for char, needed in word_count.items():
            if board_count[char] < needed:
                return False
            
    
        visited = set()
        def check(i: int, r: int, c: int) -> bool:
            if i == len(word):
                return True
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] != word[i]
            ):
                return False

            visited.add((r, c))

            found = (
                check(i + 1, r + 1, c) or
                check(i + 1, r - 1, c) or
                check(i + 1, r, c + 1) or
                check(i + 1, r, c - 1)
            )

            visited.remove((r, c))
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and check(0, i, j):
                    return True

        return False