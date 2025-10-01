class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # traverse the intervals array
        # keep a res array
        # newInterval < current interval: add the newInterval and add current interval to res
        # newInterval > current interval: ad the current interval to res
        # newInterval overlaps with the current interval: start = min(s1, s2), end = max(e1, e2)
        # edge case: add newInterval if haven't

        res = []
        inserted = False
        s2, e2 = newInterval
        for s1, e1 in intervals:
            # newInterval before
            if e2 < s1:
                if not inserted:
                    res.append([s2, e2])  
                    inserted = True
                res.append([s1, e1])
            # newInterval after
            elif s2 > e1:
                res.append([s1, e1])
            # overlap
            else:
                s2 = min(s1, s2)
                e2 = max(e1, e2)
        
        if not inserted:
            res.append([s2, e2])
        
        return res