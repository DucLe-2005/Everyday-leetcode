class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls, colors = {}, {}
        res, distinct = [], 0
        for pos, c in queries:
            if pos in balls:
                colors[balls[pos]] -= 1
                if colors[balls[pos]] == 0:
                    distinct -= 1
                
            colors[c] = colors.get(c, 0) + 1
            balls[pos] = c
            if colors[c] == 1:
                distinct += 1
            res.append(distinct)

        return res
