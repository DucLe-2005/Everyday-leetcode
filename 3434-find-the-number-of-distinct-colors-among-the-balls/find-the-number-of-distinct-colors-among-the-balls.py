class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # ball_colors: ball -> color
        # color_count: color -> count
        # if color_count[color] == 0: total_colors -= 1

        ball_colors = {}
        color_count = {}
        res = []

        for ball, new_color in queries:
            prev_color = ball_colors.get(ball, -1)
            
            if prev_color in color_count:
                color_count[prev_color] -= 1        
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            
            ball_colors[ball] = new_color
            color_count[new_color] = color_count.get(new_color, 0) + 1

            res.append(len(color_count))
        
        return res
