class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                d = board[r][c]

                if d == ".":
                    continue

                if (
                    d in cols[c] or
                    d in rows[r] or
                    d in squares[(r // 3, c // 3)]
                ):
                    return False

                cols[c].add(d)
                rows[r].add(d)
                squares[(r // 3, c // 3)].add(d)

        return True
