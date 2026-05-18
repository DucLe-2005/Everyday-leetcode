class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # time: O(1), since size of board is fixed at 9x9
        # space: O(1)

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                val = board[i][j]
                box_idx = i // 3 * 3 + j // 3

                if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)
        
        return True


