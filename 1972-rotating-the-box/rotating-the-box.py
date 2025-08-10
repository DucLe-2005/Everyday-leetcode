class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        res = [["." for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res[i][j] = boxGrid[j][i]
        
        for row in res:
            row.reverse()
        
        # apply gravity to each column, from right to left
        for c in range(m):

            # process each cell in column 'c' from bottom up
            lowest_empty = n - 1
            for i in range(n - 1, -1, -1):
                if res[i][c] == "#": 
                    res[i][c] = "."
                    res[lowest_empty][c] = "#"
                    lowest_empty -= 1

                if res[i][c] == "*":  # if obstacle is found, move lowest_empty to bove it
                    lowest_empty = i - 1

        return res