class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        step = 1  # 1: move down, -1: move up
        idx = 0

        for char in s:
            print(idx)
            rows[idx].append(char)
            if idx == 0:
                step = 1  # bounce to go down
            if idx == numRows - 1:
                step = -1  # bounce to go up
            idx += step

        return "".join("".join(row) for row in rows)