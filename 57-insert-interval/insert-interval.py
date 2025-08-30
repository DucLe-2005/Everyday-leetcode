class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s, e = newInterval
        inserted = False
        for start, end in intervals:
            if end < s:
                # current interval ends before newInterval starts
                res.append([start, end])
            elif start > e:
                # current interval starts after newInterval ends
                if not inserted:
                    res.append([s, e])
                    inserted = True
                res.append([start, end])
            else:
                # overlap -> merge to [s, e]
                s = min(start, s)
                e = max(end, e)
        
        if not inserted:
            res.append([s, e])
            
        return res