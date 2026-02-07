class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = [1]
        for _ in range(rowIndex):
            new_row = [curr[0]]
            for i in range(len(curr) - 1):
                new_row.append(curr[i] + curr[i+1])
            new_row.append(curr[-1])
            curr = new_row
        return curr
