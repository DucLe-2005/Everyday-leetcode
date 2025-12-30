class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        new_s, new_e = newInterval
        inserted = False
        for curr_s, curr_e in intervals:
            # New interval appears before
            if new_e < curr_s:
                if not inserted:
                    res.append([new_s, new_e])
                    inserted = True
                res.append([curr_s, curr_e])
            # New interval appears after
            elif new_s > curr_e:
                res.append([curr_s, curr_e])
            # New interval overlaps with current interval
            else:
                new_s = min(curr_s, new_s)
                new_e = max(curr_e, new_e)
        
        if not inserted:
            res.append([new_s, new_e])
        
        return res


            