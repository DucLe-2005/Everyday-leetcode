class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # current point = points[0]
        # iterate point in points[1:]
        # while current point != point:
        # perform each of the following actions:
        # modify y by 1 (move vertically)
        # modify x by 1 (move horizontally)
        # modify both x, y by 1 (move diagonally)
        # then increase time by 1

        res = 0
        curr = points[0]
        def update_x(src, dst):
            if src[0] < dst[0]:
                src[0] += 1
            else:
                src[0] -= 1
        
        def update_y(src, dst):
            if src[1] < dst[1]:
                src[1] += 1
            else:
                src[1] -= 1

        for p in points[1:]:
            while curr != p:
                if curr[0] != p[0] and curr[1] != p[1]:
                    update_x(curr, p)
                    update_y(curr, p)
                    res += 1
                elif curr[0] != p[0]:
                    update_x(curr, p)
                    res += 1
                elif curr[1] != p[1]:
                    update_y(curr, p)
                    res += 1
        return res
        