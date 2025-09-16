class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls, colors = defaultdict(int), defaultdict(int)  # ball : color; color : count
        res, distinct = [], 0
        for ball, color in queries:
            if ball in balls:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    distinct -= 1
            
            balls[ball] = color
            colors[color] += 1
            
            if colors[color] == 1:  # if a new color is added, one more distinct color found
                distinct += 1

            res.append(distinct)

        return res
